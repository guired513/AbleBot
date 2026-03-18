from flask import Flask, request, jsonify
from api.chatbot_logic import get_bot_response
from api.audio_pipeline import transcribe_audio_file
from api.image_reader import extract_text_from_image_file

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "AbleBot backend is running."})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({"error": "No message provided."}), 400

    response = get_bot_response(user_input)
    return jsonify({"response": response})

@app.route("/stt", methods=["POST"])
def stt():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file uploaded."}), 400

    audio_file = request.files["audio"]
    result = transcribe_audio_file(audio_file)
    return jsonify({"transcription": result})

@app.route("/ocr", methods=["POST"])
def ocr():
    if "image" not in request.files:
        return jsonify({"error": "No image file uploaded."}), 400

    image_file = request.files["image"]
    result = extract_text_from_image_file(image_file)
    return jsonify({"text": result})

if __name__ == "__main__":
    app.run(debug=True)