from fastapi import FastAPI
from pydantic import BaseModel
from main import run_rune

app = FastAPI()
chats = {}

class ChatRequest(BaseModel):
    session_id: str
    message: str


def chat(request: ChatRequest):
    if not request.session_id in chats:
        chats[request.session_id] = []

    response, messages = run_rune(request.message, chats[request.session_id])

    return response

app.add_api_route("/chat", chat, methods=["POST"])
