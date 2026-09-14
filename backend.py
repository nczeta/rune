from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from main import run_rune

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

chats = {}

class ChatRequest(BaseModel):
    session_id: str
    message: str


def chat(request: ChatRequest):
    if not request.session_id in chats:
        chats[request.session_id] = []

    response, messages = run_rune(request.message, chats[request.session_id])

    return response


def frontend():
    return FileResponse("rune_v4.html")


app.add_api_route("/chat", chat, methods=["POST"])
app.add_api_route("/", frontend, methods=["GET"])