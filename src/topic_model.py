# src/topic_model.py

from sklearn.decomposition import LatentDirichletAllocation
import numpy as np


def build_lda_model(doc_vectors, n_topics=3):
    lda = LatentDirichletAllocation(
        n_components=n_topics,
        random_state=42,
        learning_method="batch"
    )
    lda.fit(doc_vectors)
    return lda


def train_lda(matrix, n_topics: int = 3):
    """
    Train LDA model on document-term matrix
    """
    lda = build_lda_model(n_topics)
    lda.fit(matrix)
    return lda


def extract_topics(lda, vectorizer, top_n_words: int = 5):
    """
    Extract top keywords for each topic
    """
    feature_names = vectorizer.get_feature_names_out()
    topics = []

    for topic_idx, topic in enumerate(lda.components_):
        top_indices = np.argsort(topic)[-top_n_words:]
        top_words = [feature_names[i] for i in top_indices]
        topics.append((topic_idx, top_words))

    return topics
