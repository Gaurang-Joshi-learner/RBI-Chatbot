import numpy as np
import re
from typing import List, Dict
from app.services.vectorstore.faiss_index import load_index
from app.services.embeddings.embedder import generate_embedding


# -------------------------
# Text utilities
# -------------------------

def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_keywords(query: str) -> List[str]:
    query = normalize(query)
    words = query.split()

    stopwords = {
        "what", "is", "are", "the", "does", "do", "under", "according",
        "to", "of", "in", "for", "and", "or", "any", "mean", "means",
        "define", "defined", "definition", "explain", "when", "how",
        "shall", "may", "can", "be"
    }

    keywords = [w for w in words if len(w) > 3 and w not in stopwords]
    return list(set(keywords))


# -------------------------
# Main retriever
# -------------------------

def retrieve_similar_chunks(
    query: str,
    topic: str | None = None,
    top_k: int = 5
) -> List[Dict]:

    index, metadata_store = load_index()

    if index.ntotal == 0:
        print("❌ FAISS index empty")
        return []

    # -------------------------
    # 1. Vector search
    # -------------------------
    query_embedding = generate_embedding(query)
    query_vector = np.array([query_embedding], dtype="float32")

    # pull many candidates, not just top_k
    search_k = min(200, index.ntotal)
    distances, indices = index.search(query_vector, search_k)

    # -------------------------
    # 2. Keyword prep
    # -------------------------
    query_norm = normalize(query)
    keywords = extract_keywords(query)

    # -------------------------
    # 3. Candidate pool
    # -------------------------
    candidates = {}

    # From vector search
    for idx in indices[0]:
        if 0 <= idx < len(metadata_store):
            candidates[idx] = metadata_store[idx]

    # From keyword scan (global fallback)
    for i, rec in enumerate(metadata_store):
        text_norm = normalize(rec["text"])
        if any(k in text_norm for k in keywords):
            candidates[i] = rec

    # -------------------------
    # 4. Scoring
    # -------------------------
    scored = []

    for idx, rec in candidates.items():
        text = rec["text"]
        text_norm = normalize(text)

        score = 0

        # Keyword match score
        for k in keywords:
            if k in text_norm:
                score += 5

        # Exact phrase boost    
        if query_norm in text_norm:
            score += 25

        # Definition pattern boost
        if re.search(r"\b(means|means any|refers to|defined as|shall mean)\b", text_norm):
            score += 15

        # Legal structure bonus
        if re.search(r"\bshall\b|\bprovided that\b|\bsubject to\b", text_norm):
            score += 5

        # Penalize garbage / TOC
        if re.search(r"table of contents|contents|chapter|section \d+\.", text_norm):
            score -= 10

        # Length sanity
        if 200 < len(text) < 2000:
            score += 3
        else:
            score -= 3

        # Always keep semantic candidates alive
        score += 1

        scored.append((score, rec))

    # -------------------------
    # 5. Sort + dedupe
    # -------------------------
    scored.sort(key=lambda x: x[0], reverse=True)

    results = []
    seen = set()

    for score, rec in scored:
        key = rec["text"][:300]
        if key in seen:
            continue
        seen.add(key)

        results.append(rec)
        if len(results) >= top_k:
            break

    # -------------------------
    # 6. Debug (keep for now)
    # -------------------------
    print("\n[RETRIEVER DEBUG]")
    print("Query:", query)
    for i, r in enumerate(results):
        print(f"\n--- Chunk {i+1} ---")
        print(r["text"][:600])

    return results
