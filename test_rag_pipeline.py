from app.services.rag.rag_pipeline import run_rag_pipeline

query = "What are the rules for Relief Savings Bonds?"

result = run_rag_pipeline(query)

print("\n===== RAG FINAL OUTPUT =====\n")
print("QUESTION:", result["question"])
print("\nANSWER:")
print(result["answer"])

print("\n----- SOURCES -----")
for src in result["sources"]:
    print(f"- {src['title']} | {src['issue_date']} | {src['source']}")
