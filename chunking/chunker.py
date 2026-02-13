"""from typing import List


def create_chunks(
    text: str,
    *,
    chunk_size: int = 1000,
    overlap: int = 150
) -> List[str]:

    Split text into overlapping chunks for RAG.
    
    if not text or len(text.strip()) < 100:
        return []

    words = text.split()
    chunks = []

    start = 0
    total_words = len(words)

    while start < total_words:
        end = start + chunk_size
        chunk_words = words[start:end]
        chunk_text = " ".join(chunk_words).strip()

        if chunk_text:
            chunks.append(chunk_text)

        start = end - overlap
        if start < 0:
            start = 0

    return chunks
    """
