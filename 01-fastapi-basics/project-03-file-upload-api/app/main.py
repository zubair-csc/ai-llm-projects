from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import upload

app = FastAPI(title="File Upload & Processing API", version="1.0.0")

# CORS for frontend integration (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the File Upload API! POST to /upload/ to process PDFs."}