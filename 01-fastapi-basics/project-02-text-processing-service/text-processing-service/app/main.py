from fastapi import FastAPI
from app.models import *
from app.services import *

app = FastAPI(title="Text Processing API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Text Processing API"}

@app.post("/clean")
def clean_endpoint(input_data: CleanTextInput):
    return {"cleaned_text": clean_text(input_data)}

@app.post("/tokenize")
def tokenize_endpoint(input_data: TokenizeInput):
    return tokenize(input_data)

@app.post("/stats")
def stats_endpoint(input_data: TextInput):
    return calculate_stats(input_data.text)

@app.get("/health")
def health():
    return {"status": "healthy"}