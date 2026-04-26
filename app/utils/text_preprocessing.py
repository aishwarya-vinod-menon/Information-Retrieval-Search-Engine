import string
import nltk
from nltk.corpus import stopwords

_stop_words = set(stopwords.words("english"))


def preprocess_query(query: str) -> str:
    words = nltk.word_tokenize(query)
    processed = [
        word.lower()
        for word in words
        if word.lower() not in _stop_words and word not in string.punctuation
    ]
    return " ".join(processed)
