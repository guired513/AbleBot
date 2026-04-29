import json
import os
import torch
from transformers import AutoTokenizer, AutoModel
from torch.nn.functional import cosine_similarity


class BertIntentService:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.intents_path = os.path.join(base_dir, "data", "intents.json")

        self.model_name = "bert-base-uncased"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModel.from_pretrained(self.model_name)

        self.intents = self._load_intents()
        self.intent_embeddings = self._build_intent_embeddings()

    def _load_intents(self):
        with open(self.intents_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data.get("intents", [])

    def _get_embedding(self, text: str):
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=128
        )

        with torch.no_grad():
            outputs = self.model(**inputs)

        # Use CLS token embedding as sentence representation
        return outputs.last_hidden_state[:, 0, :]

    def _build_intent_embeddings(self):
        intent_embeddings = []

        for intent in self.intents:
            if intent.get("tag") == "fallback":
                continue

            patterns = intent.get("patterns", [])

            for pattern in patterns:
                embedding = self._get_embedding(pattern)

                intent_embeddings.append({
                    "tag": intent.get("tag"),
                    "pattern": pattern,
                    "embedding": embedding,
                    "responses": intent.get("responses", [])
                })

        return intent_embeddings

    def predict_intent_bert(self, text: str):
        user_embedding = self._get_embedding(text)

        best_match = None
        best_score = -1

        for item in self.intent_embeddings:
            score = cosine_similarity(
                user_embedding,
                item["embedding"]
            ).item()

            if score > best_score:
                best_score = score
                best_match = item

        if best_match is None:
            return {
                "intent": "fallback",
                "confidence": 0.0,
                "response": "I am still learning. Please try asking about PWD ID, PhilHealth, or PWD benefits.",
                "model_used": "bert"
            }

        # Temporary threshold for prototype
        if best_score < 0.60:
            return {
                "intent": "fallback",
                "confidence": round(best_score, 2),
                "response": "I am still learning. Please try asking about PWD ID, PhilHealth, or PWD benefits.",
                "model_used": "bert"
            }

        responses = best_match.get("responses", [])
        response = responses[0] if responses else "Intent detected, but no response is available."

        return {
            "intent": best_match["tag"],
            "confidence": round(best_score, 2),
            "matched_pattern": best_match["pattern"],
            "response": response,
            "model_used": "bert"
        }