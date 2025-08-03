from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from config import Config
from middlewares import setup_middlewares

Config.validate()

client = Groq(api_key=Config.GROQ_API_KEY)

app = FastAPI()

setup_middlewares(app)

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
            model=Config.GROQ_MODEL,
            temperature=0.5,
            max_tokens=300
        )

        response_message = chat_completion.choices[0].message.content

        return {"response": response_message}

    except Exception as e:
        return {"error": str(e)}
    

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)