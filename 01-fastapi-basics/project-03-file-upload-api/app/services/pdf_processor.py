import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from typing import List, Tuple

# Download NLTK data (run once)
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

class PDFProcessor:
    @staticmethod
    def extract_text(file_path: str) -> str:
        """Extract text from PDF file."""
        try:
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ''
                for page in reader.pages:
                    text += page.extract_text() + '\n'
                return text.strip()
        except Exception as e:
            raise ValueError(f"Error extracting text: {str(e)}")

    @staticmethod
    def process_text(text: str, top_n: int = 5) -> Tuple[int, List[str]]:
        """Process text: count words and extract top keywords."""
        tokens = word_tokenize(text.lower())
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
        
        word_count = len(tokens)
        keyword_counts = Counter(filtered_tokens)
        top_keywords = [word for word, _ in keyword_counts.most_common(top_n)]
        
        return word_count, top_keywords