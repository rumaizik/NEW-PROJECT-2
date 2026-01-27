NLP Topic Modeling & Search Engine (TF-IDF + LDA)

A modular Natural Language Processing project that performs topic modeling using TF-IDF vectorization + Latent Dirichlet Allocation (LDA) and provides a simple search interface over documents.

This project is designed with clean code structure, separation of concerns, and production-style organization, suitable for learning, evaluation, and extension.

Features

📄 Load and preprocess text documents

🧹 Clean text (lowercasing, punctuation removal, normalization)

🔢 Convert text into TF-IDF document–term matrix

🧠 Discover latent topics using LDA

🔎 Search documents using cosine similarity

🧩 Modular, extensible codebase (easy to add new models)

Project Structure

NEW-PROJECT-2/
│
├── data/
│   └── documents.txt          # Input text corpus (one document per line)
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py       # Text cleaning & document loading
│   ├── vectorizer.py           # TF-IDF vectorization
│   ├── topic_model.py          # LDA topic modeling
│   └── search_engine.py        # Search over documents
│
├── main.py                     # Entry point
├── requirements.txt            # Dependencies
├── .gitignore
└── README.md

Installation
1️⃣ Clone the repository
git clone https://github.com/rumaizik/NEW-PROJECT-2.git
cd NEW-PROJECT-2
2️⃣ Install dependencies
pip install -r requirements.txt

▶️ How to Run
python main.py

Output:

Discovered topics with top keywords

Interactive prompt to enter a search query

Ranked documents based on relevance

Input Format

The file data/documents.txt should contain:

One document per line.
Each line is treated as a separate document.


Example:

Machine learning is transforming artificial intelligence.
Natural language processing helps computers understand text.
Topic modeling discovers hidden patterns in documents.

Topic Modeling (LDA)

Vectorization: TF-IDF

Topic Model: Latent Dirichlet Allocation

Configurable number of topics

Reproducible results using fixed random state

Example output:

=== TOPICS DISCOVERED ===
Topic 1: ['models', 'search', 'vector', 'space', 'engines']
Topic 2: ['hidden', 'discovers', 'transforming', 'intelligence']
Topic 3: ['science', 'data', 'learning', 'used', 'widely']

 Search Engine

Uses vector similarity over TF-IDF space

Returns most relevant documents for a query

Designed to mimic basic information retrieval systems

Enter search query: machine learning

🧩Design Philosophy

Modular: Each component has a single responsibility

Extensible: Easy to swap TF-IDF, LDA, or add embeddings

Readable: Clear function names and structure

Educational + Practical: Suitable for learning and demos

🚀 Possible Extensions

Replace TF-IDF with Word2Vec / Sentence Transformers

Add Streamlit UI

Support larger datasets

Add topic coherence metrics

Persist trained models

👨‍💻 Author

Rumaiz Ibrahim K
M.Tech (Industrial Mathematics & Scientific Computing), IIT Madras


📜 License

This project is for educational and academic use.