import json
import csv
import os
from collections import Counter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INTENTS_PATH = os.path.join(BASE_DIR, "data", "intents.json")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "training_data.csv")

def main():
    with open(INTENTS_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    rows = []

    for intent in data.get("intents", []):
        tag = intent.get("tag")

        if tag == "fallback":
            continue

        for pattern in intent.get("patterns", []):
            pattern = pattern.strip()

            if pattern:
                rows.append({
                    "text": pattern,
                    "label": tag
                })

    with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["text", "label"])
        writer.writeheader()
        writer.writerows(rows)

    label_counts = Counter(row["label"] for row in rows)

    print("Training dataset exported successfully.")
    print(f"Output file: {OUTPUT_PATH}")
    print(f"Total samples: {len(rows)}")
    print("\nSamples per intent:")

    for label, count in label_counts.items():
        print(f"- {label}: {count}")

if __name__ == "__main__":
    main()