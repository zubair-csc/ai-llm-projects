# Simple Chat API

This is a beginner-friendly **FastAPI** project that implements a simple chat API. It demonstrates how to build an API with **request/response models** using Pydantic.

---

## 🚀 Features

- `GET /` → Root endpoint with a welcome message
- `POST /chat` → Accepts a user message and returns a response
- Auto-generated interactive API documentation
- Input validation with Pydantic models

---

## 🛠️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- [Pydantic](https://docs.pydantic.dev/) - Data validation using Python type annotations
- [Uvicorn](https://www.uvicorn.org/) - Lightning-fast ASGI server

---

## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ai-llm-projects.git
   cd ai-llm-projects/01-fastapi-basics/project-01-simple-chat-api
   ```

2. **Create and activate virtual environment**:
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install fastapi uvicorn
   ```

4. **Run the development server**:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

---

## 📁 Project Structure

```
project-01-simple-chat-api/
├── main.py              # Main FastAPI application
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

---

## 💻 Code Implementation

### main.py
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Simple Chat API",
    description="A beginner-friendly chat API built with FastAPI",
    version="1.0.0"
)

# Request model
class ChatMessage(BaseModel):
    message: str

# Response model
class ChatResponse(BaseModel):
    response: str

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Simple Chat API. Use POST /chat to send a message."
    }

@app.post("/chat", response_model=ChatResponse)
async def chat(chat_message: ChatMessage):
    return ChatResponse(response=f"You said: {chat_message.message}")
```

### requirements.txt
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
```

---

## 🔗 API Endpoints

### Root Endpoint
**GET** `/`

**Response:**
```json
{
  "message": "Welcome to the Simple Chat API. Use POST /chat to send a message."
}
```

### Chat Endpoint
**POST** `/chat`

**Request Body:**
```json
{
  "message": "Hello, how are you?"
}
```

**Response:**
```json
{
  "response": "You said: Hello, how are you?"
}
```

---

## 🧪 Testing the API

### Using cURL
```bash
# Test root endpoint
curl -X GET "http://127.0.0.1:8000/"

# Test chat endpoint
curl -X POST "http://127.0.0.1:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello World!"}'
```

### Using Python requests
```python
import requests

# Test root endpoint
response = requests.get("http://127.0.0.1:8000/")
print(response.json())

# Test chat endpoint
response = requests.post(
    "http://127.0.0.1:8000/chat",
    json={"message": "Hello World!"}
)
print(response.json())
```

---

## 📖 API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc** → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
- **OpenAPI Schema** → [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

---

## 🚀 Next Steps

Enhance your API with these features:

1. **Add more endpoints** (user management, message history)
2. **Implement database integration** (SQLite, PostgreSQL)
3. **Add authentication** (JWT tokens, OAuth2)
4. **Implement real chat logic** (AI integration, chatbot responses)
5. **Add error handling** and input validation
6. **Deploy to cloud** (Heroku, AWS, DigitalOcean)

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🆘 Troubleshooting

### Common Issues

**Port already in use:**
```bash
# Use a different port
uvicorn main:app --reload --port 8001
```

**Module not found:**
```bash
# Make sure you're in the correct directory and virtual environment is activated
pip list  # Check installed packages
```

**CORS issues (when testing from browser):**
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```