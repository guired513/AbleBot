from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from api.chatbot_logic import get_bot_response
from api.audio_pipeline import transcribe_audio
from api.image_reader import extract_text_from_image

app = FastAPI(title="AbleBot API", version="1.0")

# Allow cross-origin requests for local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict this in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AbleBot API is live."}

@app.post("/chat")
async def chat(user_input: str):
    reply = get_bot_response(user_input)
    return {"response": reply}

@app.post("/stt")
async def speech_to_text(file: UploadFile = File(...)):
    text = transcribe_audio(await file.read())
    return {"transcription": text}

@app.post("/ocr")
async def ocr_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    text = extract_text_from_image(image_bytes)
    return {"text": text}