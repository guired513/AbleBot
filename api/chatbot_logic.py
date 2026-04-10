from services.intent_service import IntentService

intent_service = IntentService()


def get_bot_response(user_input: str) -> str:
    """Get chatbot response using the intent service."""
    return intent_service.get_response(user_input)