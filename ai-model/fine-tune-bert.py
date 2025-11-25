# ablebot_fine_tune.py

from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset, Dataset
import torch

# 1. Load tokenizer and model
model_name = "bert-base-multilingual-cased"  # Supports Tagalog
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=5)

# 2. Sample synthetic dataset 
data = {
    "text": ["Ano ang benepisyo ng PWD?", "Paano ako makakakuha ng PhilHealth?", "May serbisyo ba para sa bulag?", "Anong karapatan ng may kapansanan?", "Kailan ang susunod na payout?"],
    "label": [0, 1, 2, 3, 4]  # Assuming  mapped intents to numeric labels
}
dataset = Dataset.from_dict(data)

# 3. Tokenization function
def tokenize_fn(example):
    return tokenizer(example['text'], padding="max_length", truncation=True)

tokenized_dataset = dataset.map(tokenize_fn)

# 4. Training arguments
training_args = TrainingArguments(
    output_dir="./bert-pwd-checkpoints",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    evaluation_strategy="no",
    save_strategy="epoch",
    logging_dir="./logs"
)

# 5. Trainer setup
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset
)

# 6. Start training
trainer.train()

# 7. Save model
trainer.save_model("ablebot-intent-classifier")
tokenizer.save_pretrained("ablebot-intent-classifier")