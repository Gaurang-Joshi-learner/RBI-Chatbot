from app.services.extraction.html_extractor import extract_rbi_html_text
from app.services.preprocessing.chunker import create_chunks
from app.services.metadata.metadata_enricher import enrich_document_metadata

URL = "https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12103"

print("===== STEP 2: CHUNKING TEST =====")

data = extract_rbi_html_text(URL)

# Minimal metadata for testing
metadata = enrich_document_metadata(
    doc_id="test123",
    title=data["title"],
    full_text=data["text"],
    document_type="MASTER_DIRECTION",
    source="RBI",
    url=URL
)

chunks = create_chunks(
    data["text"],
    metadata=metadata,
    max_chars=1000,
    overlap=150
)

print(f"Total chunks: {len(chunks)}\n")

for i, chunk in enumerate(chunks[:2]):
    print(f"--- Chunk {i} ---")
    print("Chunk ID:", chunk["chunk_id"])
    print("Metadata keys:", chunk["metadata"].keys())
    print(chunk["text"][:400])
    print()
