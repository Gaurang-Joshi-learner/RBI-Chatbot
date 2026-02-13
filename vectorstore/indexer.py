import os
from pathlib import Path
import numpy as np

from app.services.vectorstore.faiss_index import load_index, save_index
from app.services.preprocessing.pdf_loader import extract_text_from_pdf
from app.services.preprocessing.chunker import create_chunks
from app.services.embeddings.embedder import generate_embedding

PDF_DIR = "storage/pdfs/rbi"


def index_all_pdfs():
    index, metadata_store = load_index()

    pdf_dir = Path(PDF_DIR)
    pdf_files = list(pdf_dir.rglob("*.pdf"))

    if not pdf_files:
        print("❌ No PDFs found in storage/pdfs/")
        return {
            "indexed_pdfs": 0,
            "indexed_chunks": 0,
            "total_vectors": index.ntotal
        }

    total_chunks = 0
    indexed_pdfs = 0

    for pdf_path in pdf_files:
        print(f"[INDEXING] {pdf_path.name}")

        try:
            raw = extract_text_from_pdf(str(pdf_path))

            # 🔥 Normalize PDF loader output
            if isinstance(raw, list):
                if len(raw) > 0 and isinstance(raw[0], dict):
                    # [{"page": 1, "text": "..."}]
                    text = "\n".join(page.get("text", "") for page in raw)
                else:
                    # ["page1 text", "page2 text"]
                    text = "\n".join(raw)
            else:
                text = raw

        except Exception as e:
            print(f"❌ Failed to read {pdf_path.name}: {e}")
            continue

        if not text or len(text.strip()) < 200:
            print(f"⚠️ Skipping empty or invalid PDF: {pdf_path.name}")
            continue

        # Basic metadata (can be improved later)
        metadata = {
            "title": pdf_path.name,
            "document_type": "RBI_PDF",
            "department": "Unknown",
            "subject_category": "Unknown",
            "issue_date": "Unknown",
            "effective_date": "Unknown",
            "source": "RBI",
            "url": "Local PDF",
            "pdf_path": str(pdf_path),
        }

        chunks = create_chunks(text, metadata)

        if not chunks:
            print(f"⚠️ No chunks created for {pdf_path.name}")
            continue

        added = 0

        for chunk in chunks:
            emb = generate_embedding(chunk["text"])

            # 🔥 CRITICAL FIX: convert to numpy
            vector = np.array([emb], dtype="float32")
            index.add(vector)

            metadata_store.append({
                **chunk["metadata"],
                "text": chunk["text"],
                "pdf_path": str(pdf_path),
            })

            added += 1

        print(f"[OK] {pdf_path.name} → {added} chunks indexed")

        total_chunks += added
        indexed_pdfs += 1

    save_index(index, metadata_store)

    return {
        "indexed_pdfs": indexed_pdfs,
        "indexed_chunks": total_chunks,
        "total_vectors": index.ntotal,
    }


if __name__ == "__main__":
    result = index_all_pdfs()
    print("✅ Indexing finished:", result)
