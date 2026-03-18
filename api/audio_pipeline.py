import os
import tempfile
import whisper

model = whisper.load_model("base")

def transcribe_audio_file(audio_file) -> str:
    try:
        suffix = os.path.splitext(audio_file.filename)[1] or ".wav"

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_audio:
            audio_file.save(temp_audio.name)
            temp_path = temp_audio.name

        result = model.transcribe(temp_path)
        os.remove(temp_path)

        return result.get("text", "").strip()

    except Exception as e:
        return f"STT error: {str(e)}"