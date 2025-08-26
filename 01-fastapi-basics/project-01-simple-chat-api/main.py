from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Simple Chat API")

# Define the request model
class ChatRequest(BaseModel):
    message: str

# Define the response model
class ChatResponse(BaseModel):
    response: str

@app.get("/")
async def root():
    return {"message": "Welcome to the Simple Chat API. Use POST /chat to send a message."}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # Basic text processing: echo the message with a prefix
    processed_response = f"You said: {request.message}"
    # Alternative example: reverse the message
    # processed_response = request.message[::-1]
    return {"response": processed_response}