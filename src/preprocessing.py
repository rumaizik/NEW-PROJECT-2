# src/preprocessing.py
import os
import re

def clean_text(text: str) -> str:
    """
    Clean input text:
    - lowercase
    - remove special characters
    - remove extra spaces
    """
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


import os

def load_documents(file_path: str) -> list:
    # Get project root directory
    base_dir = os.path.dirname(os.path.dirname(__file__))

    # Build absolute path to data file
    full_path = os.path.join(base_dir, file_path)

    # IMPORTANT: use full_path here
    with open(full_path, "r", encoding="utf-8") as f:
        documents = f.readlines()

    cleaned_docs = [clean_text(doc) for doc in documents if doc.strip()]
    return cleaned_docs

