# app/services/vectorstore/faiss_index.py

import faiss
import os
import pickle

FAISS_DIR = "app/storage/faiss"
INDEX_PATH = os.path.join(FAISS_DIR, "rbi.index")
META_PATH = os.path.join(FAISS_DIR, "rbi_meta.pkl")

os.makedirs(FAISS_DIR, exist_ok=True)


def load_index(dim: int = 384):
    """
    Loads FAISS index + metadata if present.
    Returns empty index otherwise.
    """

    if os.path.exists(INDEX_PATH) and os.path.exists(META_PATH):
        index = faiss.read_index(INDEX_PATH)
        with open(META_PATH, "rb") as f:
            metadata = pickle.load(f)
        return index, metadata

    # Safe fallback
    index = faiss.IndexFlatL2(dim)
    metadata = []
    return index, metadata


def save_index(index, metadata):
    faiss.write_index(index, INDEX_PATH)
    with open(META_PATH, "wb") as f:
        pickle.dump(metadata, f)
def deduplicate_chunks(chunks):
    seen = set()
    unique = []

    for chunk in chunks:
        key = chunk["text"][:300]
        if key not in seen:
            seen.add(key)
            unique.append(chunk)

    return unique

