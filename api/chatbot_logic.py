import os
import random

from services.intent_service import IntentService
from services.bert_intent_service import BertIntentService
from api.bert_finetuned_service import predict_intent_finetuned

intent_service = IntentService()
rule_based_service = intent_service

try:
    bert_service = BertIntentService()
except Exception as e:
    print(f"BERT service could not be loaded: {e}")
    bert_service = None


def get_response_from_intent(intent_tag: str, confidence: float, model_used: str) -> dict:
    matched_intent = next(
        (intent for intent in intent_service.intents if intent.get("tag") == intent_tag),
        None
    )

    if matched_intent:
        responses = matched_intent.get("responses", [])
        response_text = random.choice(responses) if responses else "Intent detected, but no response is available."

        return {
            "response": response_text,
            "intent": intent_tag,
            "confidence": round(confidence, 2),
            "model_used": model_used
        }

    return {
        "response": "I understood your message, but I could not find a matching response.",
        "intent": intent_tag,
        "confidence": round(confidence, 2),
        "model_used": model_used
    }


def get_bot_response(user_input: str, mode: str = "rule-based") -> dict:
    selected_mode = mode or os.getenv("CHATBOT_MODE", "rule-based")

    if selected_mode == "bert-ft":
        intent, confidence = predict_intent_finetuned(user_input)
        return get_response_from_intent(intent, confidence, "bert-finetuned")

    if selected_mode == "bert":
        if bert_service is None:
            return {
                "response": "BERT mode is currently unavailable.",
                "intent": "bert_unavailable",
                "confidence": 0.0,
                "model_used": "bert"
            }

        return bert_service.predict_intent_bert(user_input)

    result = rule_based_service.get_response(user_input)

    if isinstance(result, str):
        return {
            "response": result,
            "intent": "rule_based_match",
            "confidence": None,
            "model_used": "rule-based"
        }

    if isinstance(result, dict):
        result["model_used"] = "rule-based"
        return result

    return {
        "response": "AbleBot could not process the request.",
        "intent": "unknown",
        "confidence": 0.0,
        "model_used": selected_mode
    }
