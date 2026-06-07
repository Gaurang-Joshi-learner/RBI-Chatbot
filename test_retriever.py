
from app.services.vectorstore.retriever import retrieve_similar_chunks

query = "What are the rules for Relief Savings Bonds?"
results = retrieve_similar_chunks(query)

print(f"\n🔍 QUERY: {query}\n")
for r in results:
    print("TEXT:", r["text"])