import os
from services.intent_service import IntentService
from services.bert_intent_service import BertIntentService

rule_based_service = IntentService()

try:
    bert_service = BertIntentService()
except Exception as e:
    print(f"BERT service could not be loaded: {e}")
    bert_service = None


def get_bot_response(user_input: str, mode: str = None) -> dict:
    selected_mode = mode or os.getenv("CHATBOT_MODE", "rule-based")

    if selected_mode == "bert":
        if bert_service is None:
            return {
                "intent": "bert_unavailable",
                "confidence": 0.0,
                "response": "BERT mode is currently unavailable. Falling back to rule-based mode.",
                "model_used": "bert"
            }

        return bert_service.predict_intent_bert(user_input)

    result = rule_based_service.get_response(user_input)

    # Safety wrapper: handles old IntentService that returns only a string
    if isinstance(result, str):
        return {
            "intent": "rule_based_match",
            "confidence": None,
            "response": result,
            "model_used": "rule-based"
        }

    result["model_used"] = "rule-based"
    return result