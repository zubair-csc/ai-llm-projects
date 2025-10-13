# File Upload & Processing API

A powerful and production-ready FastAPI-based microservice for handling PDF document uploads, text extraction, and intelligent processing. Extract text from PDFs, analyze word frequencies, identify keywords, and get comprehensive document statistics.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green)
![PyPDF2](https://img.shields.io/badge/PyPDF2-Latest-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- 📤 **Secure File Upload**: Multipart/form-data support with PDF validation
- 📝 **Text Extraction**: Complete PDF text extraction using PyPDF2
- 🔍 **Keyword Analysis**: Extract top 5 keywords with stopword filtering
- 📊 **Document Statistics**: Word count, character analysis, and more
- 🏥 **Health Monitoring**: Built-in health check endpoint
- 🐳 **Docker Ready**: Easy deployment with Docker support
- 📚 **Auto-Generated Docs**: Interactive Swagger UI and ReDoc
- ✅ **Tested**: Comprehensive pytest integration

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- pip

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/zubair-csc/project-03-file-upload-api.git
cd project-03-file-upload-api
```

2. **Set up virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the server**
```bash
python run.py
```

5. **Access the services**
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## 📁 Project Structure

```
project-03-file-upload-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI application
│   ├── models.py                  # Pydantic models
│   ├── routers/
│   │   └── upload.py             # Upload routes
│   └── services/
│       └── pdf_processor.py      # PDF processing logic
│
├── tests/
│   ├── __init__.py
│   └── test_upload.py            # API tests
│
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Docker configuration
├── run.py                        # Local development server
├── .gitignore
└── README.md
```

## 🔌 API Endpoints

### Base URL: `http://localhost:8000`

| Endpoint | Method | Description | Request | Response |
|----------|--------|-------------|---------|----------|
| `/` | GET | Root welcome message | None | Welcome JSON |
| `/upload/` | POST | Upload and process PDF | PDF file (multipart) | Processing results |
| `/health` | GET | Service health check | None | Health status |

### Example API Usage

#### Upload and Process PDF
```bash
curl -X POST "http://localhost:8000/upload/" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/path/to/document.pdf;type=application/pdf"
```

**Response:**
```json
{
  "filename": "document.pdf",
  "word_count": 150,
  "top_keywords": ["api", "fastapi", "pdf", "extraction", "nltk"],
  "extracted_text": "Sample extracted text from PDF... (truncated to 500 characters)"
}
```

#### Health Check
```bash
curl -X GET "http://localhost:8000/health"
```

**Response:**
```json
{
  "status": "healthy"
}
```

#### Root Endpoint
```bash
curl -X GET "http://localhost:8000/"
```

**Response:**
```json
{
  "message": "Welcome to the File Upload & Processing API"
}
```

## 📊 Response Schema

### Upload Response (`ProcessingResult`)

| Field | Type | Description |
|-------|------|-------------|
| `filename` | string | Original filename of uploaded PDF |
| `word_count` | integer | Total number of words in document |
| `top_keywords` | array[string] | Top 5 most frequent keywords (stopwords excluded) |
| `extracted_text` | string | First 500 characters of extracted text |

## 🐳 Docker Deployment

### Build and Run with Docker

```bash
# Build the image
docker build -t file-upload-api .

# Run the container
docker run -p 8000:8000 file-upload-api
```

### Using Docker Compose (Optional)

Create a `docker-compose.yml`:

```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - APP_NAME=File Upload API
      - DEBUG=false
    volumes:
      - ./uploads:/app/uploads
```

Run with:
```bash
docker-compose up --build
```

## 🧪 Testing

Run tests using pytest:

```bash
# Install test dependencies (if not already installed)
pip install pytest pytest-cov

# Run all tests
pytest tests/ -v

# Run with coverage report
pytest tests/ --cov=app --cov-report=html

# Run specific test file
pytest tests/test_upload.py -v
```

### Adding Test Files

Place sample PDFs in `tests/` directory:
```
tests/
├── test_upload.py
└── sample.pdf          # Add sample PDF for integration tests
```

## 📦 Dependencies

### Core Dependencies
- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: Lightning-fast ASGI server
- **PyPDF2**: PDF text extraction library
- **NLTK**: Natural Language Toolkit for text processing
- **Python-multipart**: Multipart form data support
- **Pydantic**: Data validation using Python type annotations

### Full list in `requirements.txt`:
```
fastapi==0.104.1
uvicorn[standard]==0.23.2
pypdf2==3.0.1
nltk==3.8.1
python-multipart==0.0.6
pytest==7.4.3
```

### NLTK Data

The following NLTK datasets are automatically downloaded on first run:
- `punkt` - Sentence tokenization
- `stopwords` - Common word filtering

## 🔧 Configuration

### Environment Variables

Create a `.env` file for configuration:

```env
APP_NAME="File Upload & Processing API"
VERSION="1.0.0"
HOST="0.0.0.0"
PORT=8000
DEBUG=false
MAX_FILE_SIZE=10485760  # 10MB in bytes
ALLOWED_EXTENSIONS=["pdf"]
```

### Customization Options

Modify `app/services/pdf_processor.py` to customize:
- Number of top keywords returned
- Text extraction length limit
- Stopword filtering behavior
- Additional NLP processing

## 🛠️ Development

### Local Development Setup

```bash
# Install in development mode
pip install -e .

# Run with auto-reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Format code
black app/ tests/

# Lint code
flake8 app/ tests/
```

### API Documentation

- **Swagger UI**: Interactive API documentation at `/docs`
- **ReDoc**: Alternative documentation at `/redoc`
- **OpenAPI Schema**: JSON schema at `/openapi.json`

## 🔒 Security Considerations

- ✅ File type validation (PDF only)
- ✅ File size limits (configurable)
- ✅ Secure file handling
- ⚠️ Consider adding: Rate limiting, authentication, virus scanning

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Guidelines

- Write tests for new features
- Follow PEP 8 style guide
- Update documentation as needed
- Ensure all tests pass before submitting PR

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Zubair**
- GitHub: [@zubair-csc](https://github.com/zubair-csc)
- Project Series: [Ai-LLm-projects](https://github.com/zubair-csc/ai-llm-projects)

## 🔗 Related Projects

This project is part of the **Ai-LLm-projects** series:
- [01-fastapi-basics](https://github.com/zubair-csc/01-fastapi-basics) - FastAPI fundamentals
- **[project-03-file-upload-api](https://github.com/zubair-csc/project-03-file-upload-api)** - This project
- More coming soon!

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [PyPDF2](https://pypdf2.readthedocs.io/) - PDF processing
- [NLTK](https://www.nltk.org/) - Natural language processing
- Open source community

## 📞 Support

If you have questions or need help:

- 📖 Check the [API Documentation](http://localhost:8000/docs)
- 🐛 Open an [issue](https://github.com/zubair-csc/project-03-file-upload-api/issues)
- 💬 Start a [discussion](https://github.com/zubair-csc/project-03-file-upload-api/discussions)

## 🗺️ Roadmap

- [ ] Support for multiple file formats (DOCX, TXT, etc.)
- [ ] Advanced NLP features (stemming, lemmatization)
- [ ] Named Entity Recognition (NER)
- [ ] Document summarization
- [ ] Batch file processing
- [ ] Asynchronous processing with Celery
- [ ] File storage integration (S3, GCS)
- [ ] User authentication and authorization
- [ ] Rate limiting
- [ ] Webhook notifications
- [ ] Export results to various formats

## 📈 Performance

- ⚡ Average processing time: < 2 seconds for typical PDFs
- 📊 Supports files up to 10MB (configurable)
- 🔄 Concurrent request handling via ASGI

## 🌟 Star History

If you find this project helpful, please consider giving it a star! ⭐

---

Made with ❤️ using FastAPI and Python | [Report Bug](https://github.com/zubair-csc/project-03-file-upload-api/issues) | [Request Feature](https://github.com/zubair-csc/project-03-file-upload-api/issues)
