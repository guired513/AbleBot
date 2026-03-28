import json
import os
import random

# Build path to intents.json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INTENTS_PATH = os.path.join(BASE_DIR, "data", "intents.json")


def load_intents():
    """Load intents from JSON file."""
    with open(INTENTS_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["intents"]


def normalize_text(text: str) -> str:
    """Lowercase and strip extra spaces."""
    return text.lower().strip()


def find_matching_intent(user_input: str, intents: list):
    """Simple keyword-based intent matching."""
    user_input = normalize_text(user_input)

    for intent in intents:
        for pattern in intent["patterns"]:
            pattern = normalize_text(pattern)
            if pattern in user_input or user_input in pattern:
                return intent

    return None


def get_bot_response(user_input: str) -> str:
    """Return chatbot response based on matched intent."""
    try:
        intents = load_intents()
        matched_intent = find_matching_intent(user_input, intents)

        if matched_intent:
            return random.choice(matched_intent["responses"])

        # fallback intent
        fallback_intent = next(
            (intent for intent in intents if intent["tag"] == "fallback"),
            None
        )

        if fallback_intent:
            return random.choice(fallback_intent["responses"])

        return "Sorry, I could not understand your request."

    except Exception as e:
        return f"Chatbot error: {str(e)}"