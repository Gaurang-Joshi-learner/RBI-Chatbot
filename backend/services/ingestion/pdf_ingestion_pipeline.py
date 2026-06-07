from app.services.preprocessing.pdf_loader import load_pdf_text
from app.services.preprocessing.pdf_metadata_parser import parse_pdf_metadata
from app.services.chunking.chunker import chunk_text
from app.services.embeddings.embedder import generate_embedding
from app.services.vectorstore.indexer import add_documents_to_index
from app.services.metadata.metadata_enricher import enrich_metadata


def ingest_pdf(pdf_path: str):
    # 1️⃣ Load text
    text = load_pdf_text(pdf_path)
    if not text.strip():
        return 0

    # 2️⃣ Extract metadata
    metadata = parse_pdf_metadata(pdf_path)

    # 3️⃣ Chunk text
    chunks = chunk_text(text)

    documents = []

    for chunk in chunks:
        embedding = generate_embedding(chunk)

        documents.append({
            "text": chunk,
            "embedding": embedding,
            **enrich_metadata(metadata)
        })

    # 4️⃣ Write to FAISS
    add_documents_to_index(documents)

    return len(documents)
