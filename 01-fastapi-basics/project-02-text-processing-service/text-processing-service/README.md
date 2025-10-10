# 📝 Text Processing Microservice

A powerful and easy-to-use text processing microservice built with **FastAPI** and **Streamlit**. This service provides various text analysis operations including cleaning, tokenization, statistics, sentiment analysis, and more.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- 🧹 **Text Cleaning**: Remove punctuation, numbers, extra whitespace, normalize unicode
- 🔤 **Tokenization**: Word, sentence, and character-level tokenization
- 📊 **Text Statistics**: Character count, word count, sentence count, and more
- 📈 **Word Frequency Analysis**: Visualize most common words
- 🔍 **N-gram Extraction**: Extract and analyze n-grams (2-5 grams)
- 😊 **Sentiment Analysis**: Rule-based sentiment classification
- 🎨 **Beautiful Web UI**: Interactive Streamlit interface with charts

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- pip

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/zubair-csc/ai-llm-projects.git
cd ai-llm-projects/01-fastapi-basics/project-02-text-processing-service/text-processing-service
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the FastAPI backend**
```bash
uvicorn app.main:app --reload
```

4. **Run the Streamlit frontend** (in a new terminal)
```bash
streamlit run app_ui.py
```

5. **Access the services**
- **Streamlit UI**: http://localhost:8501
- **FastAPI Docs**: http://localhost:8000/docs
- **API Health Check**: http://localhost:8000/health

## 📁 Project Structure

```
text-processing-service/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── models.py            # Pydantic models
│   └── services.py          # Business logic
│
├── tests/
│   └── test_api.py          # API tests
│
├── app_ui.py                # Streamlit web interface
├── requirements.txt         # Python dependencies
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose setup
├── .gitignore
└── README.md
```

## 🔌 API Endpoints

### Base URL: `http://localhost:8000`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Root endpoint |
| `/clean` | POST | Clean and normalize text |
| `/tokenize` | POST | Tokenize text |
| `/stats` | POST | Calculate text statistics |
| `/word-frequency` | POST | Get word frequency distribution |
| `/ngrams` | POST | Extract n-grams |
| `/sentiment` | POST | Analyze sentiment |
| `/health` | GET | Health check |

### Example API Usage

#### Clean Text
```bash
curl -X POST "http://localhost:8000/clean"   -H "Content-Type: application/json"   -d '{
    "text": "Hello WORLD!!! 123",
    "lowercase": true,
    "remove_punctuation": true,
    "remove_numbers": true
  }'
```

**Response:**
```json
{
  "cleaned_text": "hello world"
}
```

#### Tokenize Text
```bash
curl -X POST "http://localhost:8000/tokenize"   -H "Content-Type: application/json"   -d '{
    "text": "This is a sample text.",
    "method": "word",
    "lowercase": false
  }'
```

**Response:**
```json
{
  "tokens": ["This", "is", "a", "sample", "text"],
  "count": 5
}
```

#### Text Statistics
```bash
curl -X POST "http://localhost:8000/stats"   -H "Content-Type: application/json"   -d '{"text": "Hello world! How are you?"}'
```

**Response:**
```json
{
  "character_count": 24,
  "character_count_no_spaces": 20,
  "word_count": 5,
  "sentence_count": 2,
  "average_word_length": 4.0,
  "unique_words": 5
}
```

#### Sentiment Analysis
```bash
curl -X POST "http://localhost:8000/sentiment"   -H "Content-Type: application/json"   -d '{"text": "This is a great product! I love it."}'
```

**Response:**
```json
{
  "sentiment": "positive",
  "score": 1.0,
  "positive_words": 2,
  "negative_words": 0
}
```

## 🎨 Web Interface

The Streamlit UI provides an intuitive interface for all text processing operations:

### Features:
- **Interactive Text Input**: Easy text entry
- **Multiple Operations**: Switch between 6 different operations
- **Visual Analytics**: Beautiful charts and graphs using Plotly
- **Real-time Processing**: Instant results
- **Customizable Options**: Configure each operation

### Screenshots:

**Text Statistics**
- Character, word, and sentence counts
- Interactive bar charts
- Average word length metrics

**Word Frequency**
- Top N most common words
- Horizontal bar charts
- Searchable data table

**Sentiment Analysis**
- Emoji-based sentiment display
- Sentiment score gauge
- Positive/negative word counts

## 🐳 Docker Deployment

### Build and Run with Docker

```bash
# Build the image
docker build -t text-processing-service .

# Run the container
docker run -p 8000:8000 text-processing-service
```

### Using Docker Compose

```bash
# Start services
docker-compose up --build

# Stop services
docker-compose down
```

## 🧪 Testing

Run tests using pytest:

```bash
# Install dev dependencies
pip install pytest pytest-asyncio httpx

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=app --cov-report=html
```

## 📦 Dependencies

### Core Dependencies
- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server
- **Pydantic**: Data validation
- **Streamlit**: Web interface
- **Plotly**: Interactive charts
- **Requests**: HTTP library

### Full list in `requirements.txt`:
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
streamlit==1.28.0
plotly==5.17.0
requests==2.31.0
```

## 🔧 Configuration

Create a `.env` file for configuration:

```env
APP_NAME="Text Processing Service"
VERSION="1.0.0"
HOST="0.0.0.0"
PORT=8000
DEBUG=false
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Zubair**
- GitHub: [@zubair-csc](https://github.com/zubair-csc)

## 🙏 Acknowledgments

- FastAPI documentation and community
- Streamlit for the amazing framework
- Contributors and users of this project

## 📞 Contact

Zubair - [GitHub Profile](https://github.com/zubair-csc)

Project Link: https://github.com/zubair-csc/ai-llm-projects/tree/main/01-fastapi-basics/project-02-text-processing-service/text-processing-service

If you have any questions or issues, please:
- Open an issue on GitHub
- Contact via email
- Check the [documentation](http://localhost:8000/docs)

## 🗺️ Roadmap

- [ ] Add more NLP features (stemming, lemmatization)
- [ ] Support for multiple languages
- [ ] Named Entity Recognition (NER)
- [ ] Text similarity comparison
- [ ] Export results to CSV/JSON
- [ ] User authentication
- [ ] Rate limiting
- [ ] Caching layer

---

⭐ **Star this repo** if you find it helpful!

Made with ❤️ using FastAPI and Streamlit
