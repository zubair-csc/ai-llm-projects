from pydantic import BaseModel
from typing import List, Optional

class UploadResponse(BaseModel):
    filename: str
    word_count: int
    top_keywords: List[str]
    extracted_text: Optional[str] = None  # Optional to avoid large responses

class ErrorResponse(BaseModel):
    detail: str