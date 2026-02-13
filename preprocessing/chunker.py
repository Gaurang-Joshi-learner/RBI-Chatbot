from typing import List, Dict
import uuid

def create_chunks(
    text: str,
    metadata: Dict,
    max_chars: int = 800,
    overlap: int = 100
) -> List[Dict]:
    """
    Split extracted RBI text into clean overlapping chunks.
    Ensures no empty or junk chunks are produced.
    """

    if not text or len(text.strip()) < 100:
        return []

    text = text.strip()
    chunks = []

    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + max_chars, text_length)

        chunk_text = text[start:end].strip()

        # 🔴 CRITICAL FIX: skip empty / junk chunks
        if len(chunk_text) < 150:
            start = end
            continue

        chunk = {
            "id": str(uuid.uuid4()),
            "text": chunk_text,
            "metadata": {
                "title": metadata.get("title"),
                "document_type": metadata.get("document_type"),
                "department": metadata.get("department"),
                "subject_category": metadata.get("subject_category"),
                "issue_date": metadata.get("issue_date"),
                "effective_date": metadata.get("effective_date"),
                "source": metadata.get("source", "RBI"),
                "url": metadata.get("url"),
            }
        }

        chunks.append(chunk)

        # move window with overlap
        start = end - overlap

    return chunks
