# src/vectorizer.py

from sklearn.feature_extraction.text import TfidfVectorizer


def build_vectorizer(documents):
    vectorizer = TfidfVectorizer(stop_words="english")
    doc_vectors = vectorizer.fit_transform(documents)
    return vectorizer, doc_vectors


def vectorize_documents(documents):
    """
    Convert text documents into TF-IDF vectors
    """
    vectorizer = build_vectorizer()
    matrix = vectorizer.fit_transform(documents)
    return matrix, vectorizer
