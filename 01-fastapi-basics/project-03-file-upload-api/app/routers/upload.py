from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import shutil
import os
from pathlib import Path
from typing import List

from app.models import UploadResponse, ErrorResponse
from app.services.pdf_processor import PDFProcessor

router = APIRouter(prefix="/upload", tags=["uploads"])

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post("/", response_model=UploadResponse)
async def upload_pdf(file: UploadFile = File(...)):
    """Upload and process a PDF file."""
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    # Save uploaded file
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    try:
        # Extract and process
        text = PDFProcessor.extract_text(file_path)
        word_count, top_keywords = PDFProcessor.process_text(text)
        
        # Clean up uploaded file
        os.unlink(file_path)
        
        return UploadResponse(
            filename=file.filename,
            word_count=word_count,
            top_keywords=top_keywords,
            extracted_text=text[:500] + "..." if len(text) > 500 else text  # Truncate for response
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}