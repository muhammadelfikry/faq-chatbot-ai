from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GRQQ_API_KEY")
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("prompt.txt", "r") as f:
    prompt = f.read()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "Hello World"}

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
    

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)