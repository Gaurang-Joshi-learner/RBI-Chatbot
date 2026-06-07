from app.services.vectorstore.faiss_index import load_index

index, meta = load_index()

print("Total vectors:", index.ntotal)
print("First record keys:", meta[0].keys())
print("Sample text:", meta[0]["text"][:300])
