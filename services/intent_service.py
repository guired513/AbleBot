import json
import os
import random


class IntentService:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.intents_path = os.path.join(base_dir, "data", "intents.json")
        self.intents = self._load_intents()

    def _load_intents(self):
        """Load intents from the JSON file."""
        try:
            with open(self.intents_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            return data.get("intents", [])
        except Exception as e:
            print(f"Error loading intents: {e}")
            return []

    def _normalize_text(self, text: str) -> str:
        """Normalize user input for matching."""
        return text.lower().strip()

    def _find_matching_intent(self, user_input: str):
        """Find the best matching intent using simple keyword matching."""
        user_input = self._normalize_text(user_input)

        for intent in self.intents:
            for pattern in intent.get("patterns", []):
                pattern = self._normalize_text(pattern)
                if pattern in user_input or user_input in pattern:
                    return intent

        return None

    def get_response(self, user_input: str) -> str:
        """Return a response based on matched intent."""
        try:
            matched_intent = self._find_matching_intent(user_input)

            if matched_intent:
                responses = matched_intent.get("responses", [])
                if responses:
                    return random.choice(responses)

            fallback_intent = next(
                (intent for intent in self.intents if intent.get("tag") == "fallback"),
                None
            )

            if fallback_intent:
                fallback_responses = fallback_intent.get("responses", [])
                if fallback_responses:
                    return random.choice(fallback_responses)

            return "Sorry, I could not understand your request."

        except Exception as e:
            return f"Intent service error: {str(e)}"