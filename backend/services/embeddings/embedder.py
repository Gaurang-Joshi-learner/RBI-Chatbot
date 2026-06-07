# app/services/embeddings/embedder.py

from typing import List
from sentence_transformers import SentenceTransformer

# Load once
_model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embedding(text: str) -> List[float]:
    """
    Generate embedding using local SentenceTransformer.
    Safe for short queries.
    """

    if not text:
        raise ValueError("Empty text cannot be embedded")

    text = text.strip()

    # Prevent crash on short queries
    if len(text) < 10:
        text = f"Query: {text}"

    embedding = _model.encode(text, normalize_embeddings=True)
    return embedding.tolist()
