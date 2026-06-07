from app.services.vectorstore.faiss_index import load_index

index, metadata = load_index()

print("Total vectors:", index.ntotal)

# Print first 20 unique pdf paths used
pdfs = set()
for rec in metadata:
    if "pdf_path" in rec:
        pdfs.add(rec["pdf_path"])

print("Total PDFs indexed:", len(pdfs))
for p in list(pdfs)[:10]:
    print(p)
