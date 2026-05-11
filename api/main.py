from flask import Flask, request, jsonify, send_from_directory
from api.chatbot_logic import get_bot_response
from api.audio_pipeline import transcribe_audio_file
from api.image_reader import extract_text_from_image_file

app = Flask(
    __name__,
    static_folder="../static",
    static_url_path="/static"
)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "AbleBot backend is running."})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    user_input = data.get("message", "").strip()
    mode = data.get("mode", "rule-based").strip()

    if not user_input:
        return jsonify({"error": "No message provided."}), 400

    result = get_bot_response(user_input, mode)
    return jsonify(result)

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

@app.route("/app")
def mobile_app():
    return send_from_directory("../static", "app.html")


@app.route("/manifest.json")
def manifest():
    return send_from_directory("../static", "manifest.json")


@app.route("/service-worker.js")
def service_worker():
    return send_from_directory("../static", "service-worker.js")

@app.route("/health", methods=["GET"])
def health():
    return {
        "success": True,
        "status": "online",
        "service": "AbleBot Flask Backend"
    }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)