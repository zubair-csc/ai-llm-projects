


# Simple Chat API

This is a beginner-friendly **FastAPI** project that implements a simple chat API.  
It demonstrates how to build an API with **request/response models** using Pydantic.

---

## 🚀 Features
- `GET /` → Root endpoint with a welcome message.
- `POST /chat` → Accepts a user message and returns a response.

---

## 🛠️ Tech Stack
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Uvicorn](https://www.uvicorn.org/) (ASGI server)

---

## 📦 Installation & Setup

1. **Clone the repository** (if not already):
   ```bash
   git clone https://github.com/your-username/ai-llm-projects.git
   cd ai-llm-projects/01-fastapi-basics/project-01-simple-chat-api
````

2. **Activate virtual environment** (if not already created):

   ```bash
   cd ..
   python -m venv venv
   source venv/Scripts/activate  # Windows
   # or
   source venv/bin/activate      # Linux/Mac
   ```

3. **Install dependencies**:

   ```bash
   pip install fastapi uvicorn
   ```

4. **Run the server**:

   ```bash
   uvicorn main:app --reload
   ```

---

## 🔗 API Endpoints

### Root

```http
GET /
```

**Response:**

```json
{
  "message": "Welcome to the Simple Chat API. Use POST /chat to send a message."
}
```

### Chat

```http
POST /chat
Content-Type: application/json
{
  "message": "Hello"
}
```

**Response:**

```json
{
  "response": "You said: Hello"
}
```

---

## 📖 Docs

FastAPI auto-generates docs:

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---
