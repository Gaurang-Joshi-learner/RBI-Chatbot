from pathlib import Path
from typing import List, Dict

from app.services.preprocessing.pdf_loader import extract_text_from_pdf
from app.services.chunking.chunker import chunk_text
from app.services.embeddings.embedder import generate_embedding
from app.services.metadata.metadata_enricher import enrich_metadata
from app.services.vectorstore.indexer import add_documents_to_index


PDF_DIR = Path("storage/pdfs/rbi")


def ingest_downloaded_pdfs() -> int:
    documents_to_index: List[Dict] = []

    for pdf_path in PDF_DIR.glob("*.pdf"):
        try:
            text = extract_text_from_pdf(pdf_path)
            if not text.strip():
                continue

            chunks = chunk_text(text)

            for chunk in chunks:
                embedding = generate_embedding(chunk)

                doc = {
                    "text": chunk,
                    "embedding": embedding,
                    "source": "RBI",
                    "file_path": str(pdf_path),
                }

                doc = enrich_metadata(doc)
                documents_to_index.append(doc)

        except Exception as e:
            print(f"[ERROR] Failed to ingest {pdf_path.name}: {e}")

    indexed = add_documents_to_index(documents_to_index)
    print(f"[INDEXED] {indexed} chunks added to FAISS")

    return indexed
