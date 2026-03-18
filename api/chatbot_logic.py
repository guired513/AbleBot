def get_bot_response(user_input: str) -> str:
    user_input = user_input.lower()

    if "philhealth" in user_input:
        return "You can apply for PhilHealth at the nearest office or through their online portal."
    elif "pwd id" in user_input:
        return "You may apply for a PWD ID at your local PDAO or municipal social welfare office."
    elif "hello" in user_input or "hi" in user_input:
        return "Hello. How can I assist you today?"
    else:
        return "I am still being trained. For now, I can help with basic accessibility and government service inquiries."