# NLP Topic Modeling and Document Search Engine

This project implements a complete **Natural Language Processing (NLP) pipeline** that performs topic modeling and semantic document search on a text corpus using classical machine learning techniques.

The system preprocesses raw text, converts it into numerical representations, discovers latent topics using LDA, and allows users to search documents based on semantic similarity.

---

## Key Features

- Text preprocessing:
  - Lowercasing
  - Punctuation removal
  - Whitespace normalization
- TF-IDF based document–term matrix construction
- Latent topic discovery using Latent Dirichlet Allocation (LDA)
- Interactive document search using cosine similarity
- Modular and extensible project structure

---

## Project Structure


## Project Structure

NEW-PROJECT-2/
├── data/
│ └── documents.txt # Input corpus (one document per line)
├── src/
│ ├── preprocessing.py # Text cleaning and document loading
│ ├── vectorizer.py # TF-IDF vectorization
│ ├── topic_model.py # LDA topic modeling
│ └── search_engine.py # Document search using cosine similarity
├── main.py # Entry point
├── requirements.txt # Python dependencies
└── README.md


---

## Workflow Overview

1. Load raw documents from `data/documents.txt`
2. Clean and normalize text data
3. Convert text into TF-IDF vectors
4. Train an LDA model to discover latent topics
5. Display top keywords for each discovered topic
6. Accept a user search query
7. Rank documents based on cosine similarity with the query

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/rumaizik/NEW-PROJECT-2.git
cd NEW-PROJECT-2
pip install -r requirements.txt

How to Run

python main.py


Output

Displays discovered topics with top keywords

Prompts the user to enter a search query

Returns documents ranked by relevance scor

Technologies Used

Python

scikit-learn

TF-IDF Vectorization

Latent Dirichlet Allocation (LDA)

Cosine Similarity

Design Philosophy

This project emphasizes:

Clear separation of responsibilities (preprocessing, modeling, search)

Readable and maintainable code

Easy extensibility for advanced NLP models (e.g., embeddings or transformers)

Author

Rumaiz Ibrahim K