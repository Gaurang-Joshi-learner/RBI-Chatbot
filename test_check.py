from app.services.vectorstore.faiss_index import load_index

index, metadata = load_index()

found = False
for rec in metadata:
    if "amount due" in rec["text"].lower():
        print("FOUND:")
        print(rec["text"][:500])
        found = True
        break

print("Found?", found)
