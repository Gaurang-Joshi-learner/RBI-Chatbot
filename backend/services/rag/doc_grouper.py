# app/services/rag/doc_grouper.py

from collections import defaultdict
from typing import List, Dict


def group_chunks_by_document(
    retrieved_chunks: List[Dict]
) -> List[Dict]:
    grouped = defaultdict(lambda: {
        "title": None,
        "issue_date": None,
        "document_type": None,
        "department": None,
        "source": None,
        "url": None,
        "chunks": [],
    })

    for chunk in retrieved_chunks:
        metadata = chunk.get("metadata", {})
        text = chunk.get("text", "").strip()

        doc_key = (
            metadata.get("title", "Unknown"),
            metadata.get("issue_date", "Unknown"),
        )

        doc = grouped[doc_key]

        doc["title"] = metadata.get("title", "Unknown")
        doc["issue_date"] = metadata.get("issue_date", "Unknown")
        doc["document_type"] = metadata.get("document_type", "Unknown")
        doc["department"] = metadata.get("department", "Unknown")
        doc["source"] = metadata.get("source", "RBI")
        doc["url"] = metadata.get("url")

        if text:
            doc["chunks"].append(text)

    documents = []
    for doc in grouped.values():
        documents.append({
            "title": doc["title"],
            "issue_date": doc["issue_date"],
            "document_type": doc["document_type"],
            "department": doc["department"],
            "source": doc["source"],
            "url": doc["url"],
           "combined_text": "\n\n".join(doc["chunks"][:3]),  # ONLY TOP 3 CHUNKS
            "chunks": doc["chunks"],
        })

    return documents
