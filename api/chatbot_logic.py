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


def get_bot_response(user_input, mode="rule-based"):

    if mode == "bert-ft":
        intent, confidence = predict_intent_finetuned(user_input)

        matched_intent = next(
            (i for i in intent_service.intents if i["tag"] == intent),
            None
        )

        if matched_intent:
            response = random.choice(matched_intent["responses"])

            return {
                "response": response,
                "intent": intent,
                "confidence": round(confidence, 2),
                "model_used": "bert-finetuned"
            }
        if confidence < 0.4:
            return {
                "response": "I'm not fully confident. Can you rephrase your question?",
                "intent": "uncertain",
                "confidence": round(confidence, 2),
                "model_used": "bert-finetuned"
            }

# def get_bot_response(user_input: str, mode: str = None) -> dict:
#     selected_mode = mode or os.getenv("CHATBOT_MODE", "rule-based")

#     if selected_mode == "bert":
#         if bert_service is None:
#             return {
#                 "intent": "bert_unavailable",
#                 "confidence": 0.0,
#                 "response": "BERT mode is currently unavailable. Falling back to rule-based mode.",
#                 "model_used": "bert"
#             }

#         return bert_service.predict_intent_bert(user_input)

#     result = rule_based_service.get_response(user_input)

#     # Safety wrapper: handles old IntentService that returns only a string
#     if isinstance(result, str):
#         return {
#             "intent": "rule_based_match",
#             "confidence": None,
#             "response": result,
#             "model_used": "rule-based"
#         }

#     result["model_used"] = "rule-based"
#     return result
