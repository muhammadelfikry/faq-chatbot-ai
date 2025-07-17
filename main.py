from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

client = Groq(
    api_key=os.getenv("GRQQ_API_KEY")
)

with open("prompt.txt", "r") as f:
    prompt = f.read()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat_bot(req: ChatRequest):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": prompt
                },
                {
                    "role": "user",
                    "content": req.message,
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
        )

        response_message = chat_completion.choices[0].message.content

        return {"response": response_message}

    except Exception as e:
        return {"error": str(e)}