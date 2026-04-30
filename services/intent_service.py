import json
import os
import random
import re


class IntentService:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.intents_path = os.path.join(base_dir, "data", "intents.json")
        self.intents = self._load_intents()

    def _load_intents(self):
        try:
            with open(self.intents_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            return data.get("intents", [])
        except Exception as e:
            print(f"Error loading intents: {e}")
            return []

    def _normalize_text(self, text: str) -> str:
        text = text.lower().strip()
        text = re.sub(r"[^\w\s]", "", text)
        return text

    def _tokenize(self, text: str):
        return self._normalize_text(text).split()

    def _score_pattern_match(self, user_input: str, pattern: str) -> float:
        user_tokens = set(self._tokenize(user_input))
        pattern_tokens = set(self._tokenize(pattern))

        if not user_tokens or not pattern_tokens:
            return 0.0

        overlap = user_tokens.intersection(pattern_tokens)
        score = len(overlap) / len(pattern_tokens)
        return score

    def _find_best_intent(self, user_input: str):
        best_intent = None
        best_score = 0.0

        for intent in self.intents:
            if intent.get("tag") == "fallback":
                continue

            for pattern in intent.get("patterns", []):
                score = self._score_pattern_match(user_input, pattern)

                if score > best_score:
                    best_score = score
                    best_intent = intent

        return best_intent, best_score

    def get_response(self, user_input: str) -> dict:
        try:
            matched_intent, confidence = self._find_best_intent(user_input)

            # 🔥 THIS IS THE THRESHOLD (you were looking for this earlier)
            if matched_intent and confidence >= 0.6:
                responses = matched_intent.get("responses", [])
                response_text = random.choice(responses) if responses else "No response available."

                return {
                    "intent": matched_intent.get("tag", "unknown"),
                    "confidence": round(confidence, 2),
                    "response": response_text
                }

            # fallback
            fallback_intent = next(
                (intent for intent in self.intents if intent.get("tag") == "fallback"),
                None
            )

            if fallback_intent:
                fallback_responses = fallback_intent.get("responses", [])
                fallback_text = random.choice(fallback_responses)

                return {
                    "intent": "fallback",
                    "confidence": round(confidence, 2),
                    "response": fallback_text
                }

            return {
                "intent": "unknown",
                "confidence": round(confidence, 2),
                "response": "Sorry, I could not understand your request."
            }

        except Exception as e:
            return {
                "intent": "error",
                "confidence": 0.0,
                "response": f"Intent service error: {str(e)}"
            }