from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ollama
from fastapi.responses import StreamingResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL = "qwen2.5-coder:7b"

class Prompt(BaseModel):
    message: str

@app.post("/chat")
def chat(prompt: Prompt):

    def stream():
        response = ollama.chat(
            model=MODEL,
            messages=[{"role": "user", "content": prompt.message}],
            stream=True
        )

        for chunk in response:
            if "message" in chunk:
                content = chunk["message"]["content"]
                yield content

    return StreamingResponse(stream(), media_type="text/plain")