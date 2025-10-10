from pydantic import BaseModel, Field

class TextInput(BaseModel):
    text: str

class CleanTextInput(BaseModel):
    text: str
    lowercase: bool = True
    remove_punctuation: bool = True

class TokenizeInput(BaseModel):
    text: str
    method: str = "word"