# api/main.py
from fastapi import FastAPI
from api.chatbot_logic import handle_chat

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AbleBot API is running"}

@app.post("/chat")
def chat_endpoint(input_data: dict):
    return handle_chat(input_data)