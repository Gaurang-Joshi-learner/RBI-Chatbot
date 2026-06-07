# test_prompt_builder.py

from app.services.rag.prompt_builder import build_rag_prompt

documents = [
    {
        "title": "Master Directions on Relief/Savings Bonds",
        "document_type": "MASTER_DIRECTION",
        "department": "DBR",
        "issue_date": "July 2, 2018",
        "source": "RBI",
        "combined_text": "Relief Savings Bonds are issued by RBI.\nThese bonds have fixed interest rates."
    },
    {
        "title": "Master Circular on NBFCs",
        "document_type": "MASTER_CIRCULAR",
        "department": "DNBR",
        "issue_date": "April 1, 2022",
        "source": "RBI",
        "combined_text": "NBFCs must comply with RBI regulations."
    }
]

result = build_rag_prompt(
    question="What are the rules for Relief Savings Bonds?",
    documents=documents
)

print("\n===== MULTI-DOCUMENT PROMPT =====\n")
print(result["prompt"])

print("\n----- SOURCES -----")
for s in result["sources"]:
    print(f"- {s['title']} | {s['issue_date']} | {s['source']}")
