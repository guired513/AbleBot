import os
import pandas as pd
import torch
import joblib
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.optim import AdamW

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "training_data.csv")
MODEL_OUTPUT_DIR = os.path.join(BASE_DIR, "models", "bert_intent_classifier")
LABEL_ENCODER_PATH = os.path.join(MODEL_OUTPUT_DIR, "label_encoder.pkl")

MODEL_NAME = "bert-base-uncased"


class IntentDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_length=128):
        self.texts = list(texts)
        self.labels = list(labels)
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        text = str(self.texts[index])
        label = int(self.labels[index])

        encoding = self.tokenizer(
            text,
            truncation=True,
            padding="max_length",
            max_length=self.max_length,
            return_tensors="pt"
        )

        return {
            "input_ids": encoding["input_ids"].squeeze(0),
            "attention_mask": encoding["attention_mask"].squeeze(0),
            "labels": torch.tensor(label, dtype=torch.long)
        }


def main():
    print("Starting AbleBot BERT fine-tuning test...")

    df = pd.read_csv(DATA_PATH)
    df = df.dropna()

    print(f"Total samples: {len(df)}")
    print("\nSamples per label:")
    print(df["label"].value_counts())

    label_encoder = LabelEncoder()
    df["label_id"] = label_encoder.fit_transform(df["label"])

    print("\nLabel mapping:")
    for idx, label in enumerate(label_encoder.classes_):
        print(f"{idx}: {label}")

    # Safer split for small dataset
    train_df, test_df = train_test_split(
        df,
        test_size=0.2,
        random_state=42
    )

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_NAME,
        num_labels=len(label_encoder.classes_)
    )

    train_dataset = IntentDataset(
        train_df["text"],
        train_df["label_id"],
        tokenizer
    )

    test_dataset = IntentDataset(
        test_df["text"],
        test_df["label_id"],
        tokenizer
    )

    train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=4)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"\nUsing device: {device}")

    model.to(device)

    optimizer = AdamW(model.parameters(), lr=2e-5)

    epochs = 3
    model.train()

    print("\nTraining started...")

    for epoch in range(epochs):
        total_loss = 0

        for batch in train_loader:
            optimizer.zero_grad()

            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            labels = batch["labels"].to(device)

            outputs = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                labels=labels
            )

            loss = outputs.loss
            total_loss += loss.item()

            loss.backward()
            optimizer.step()

        avg_loss = total_loss / len(train_loader)
        print(f"Epoch {epoch + 1}/{epochs} - Average loss: {avg_loss:.4f}")

    print("\nEvaluating...")
    model.eval()

    correct = 0
    total = 0

    with torch.no_grad():
        for batch in test_loader:
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            labels = batch["labels"].to(device)

            outputs = model(
                input_ids=input_ids,
                attention_mask=attention_mask
            )

            predictions = torch.argmax(outputs.logits, dim=1)

            correct += (predictions == labels).sum().item()
            total += labels.size(0)

    accuracy = correct / total if total > 0 else 0

    print(f"Test accuracy: {accuracy:.4f}")

    print("\nSaving model...")
    os.makedirs(MODEL_OUTPUT_DIR, exist_ok=True)

    model.save_pretrained(MODEL_OUTPUT_DIR)
    tokenizer.save_pretrained(MODEL_OUTPUT_DIR)
    joblib.dump(label_encoder, LABEL_ENCODER_PATH)

    print("BERT fine-tuning test completed.")
    print(f"Model saved to: {MODEL_OUTPUT_DIR}")
    print(f"Label encoder saved to: {LABEL_ENCODER_PATH}")


if __name__ == "__main__":
    main()