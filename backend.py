from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str


def home():
    return {"message": "RUNE API"}


app.add_api_route("/", home, methods=["GET"])