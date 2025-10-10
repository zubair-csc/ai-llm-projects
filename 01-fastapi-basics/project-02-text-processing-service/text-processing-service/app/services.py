import re
from collections import Counter

def clean_text(input_data):
    text = input_data.text
    if input_data.lowercase:
        text = text.lower()
    if input_data.remove_punctuation:
        text = re.sub(r'[^\w\s]', ' ', text)
    return re.sub(r'\s+', ' ', text).strip()

def tokenize(input_data):
    if input_data.method == "word":
        tokens = re.findall(r'\b\w+\b', input_data.text)
    elif input_data.method == "sentence":
        tokens = re.split(r'[.!?]+', input_data.text)
    return {"tokens": tokens, "count": len(tokens)}

def calculate_stats(text):
    words = re.findall(r'\b\w+\b', text)
    return {
        "character_count": len(text),
        "word_count": len(words),
        "unique_words": len(set(words))
    }