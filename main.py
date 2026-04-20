from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app=FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "hello"}


api_key=os.getenv("OPENROUTER_API_KEY")

client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
    )

@app.post("/chat")
async def bot(request: ChatRequest):
    response=client.chat.completions.create(
        model="google/gemma-3-12b-it:free", 
        messages=[{"role": "user", "content": request.message}]
    )
    return {"response": response.choices[0].message.content}
