# src/main.py

from src.preprocessing import load_documents
from src.vectorizer import build_vectorizer
from src.topic_model import build_lda_model
from src.search_engine import search


def main():
    # Load documents
    documents = load_documents("data/documents.txt")

    # Vectorize text
    vectorizer, doc_vectors = build_vectorizer(documents)

    # Topic Modeling
    lda_model = build_lda_model(doc_vectors, n_topics=3)

    print("\n=== TOPICS DISCOVERED ===")
    feature_names = vectorizer.get_feature_names_out()

    for idx, topic in enumerate(lda_model.components_):
        top_words = [feature_names[i] for i in topic.argsort()[-5:]]
        print(f"Topic {idx + 1}: {top_words}")

    # Search
    query = input("\nEnter search query: ")
    results = search(query, documents, doc_vectors, vectorizer)

    print("\n=== SEARCH RESULTS ===")
    for doc, score in results:
        print(f"Score: {round(score, 3)} | {doc}")


if __name__ == "__main__":
    main()
