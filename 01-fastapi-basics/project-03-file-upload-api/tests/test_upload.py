import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_endpoint():
    with open("sample.pdf", "rb") as f:  # Assume you have a sample.pdf in tests/
        response = client.post("/upload/", files={"file": ("sample.pdf", f, "application/pdf")})
    assert response.status_code == 200
    assert "word_count" in response.json()