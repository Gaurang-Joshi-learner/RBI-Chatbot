from app.services.vectorstore.faiss_index import load_index

index, metadata = load_index()

print("\n📦 FAISS INDEX INSPECTION")
print("--------------------------------")
print(f"Total vectors in index: {index.ntotal}")
print(f"Total metadata records: {len(metadata)}")

if metadata:
    print("\n🔎 Sample metadata:")
    print(metadata[0])
