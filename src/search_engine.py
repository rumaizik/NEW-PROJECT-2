# src/search_engine.py

from sklearn.metrics.pairwise import cosine_similarity
from src.preprocessing import clean_text


def search(query, documents, doc_vectors, vectorizer, top_k=3):
    """
    Search documents using cosine similarity
    """
    query = clean_text(query)
    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(query_vector, doc_vectors).flatten()
    ranked_indices = similarities.argsort()[::-1][:top_k]

    results = []
    for idx in ranked_indices:
        results.append((documents[idx], similarities[idx]))

    return results
