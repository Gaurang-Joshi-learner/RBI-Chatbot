from app.services.rag.timeline_answer_generator import generate_timeline_answer
from app.services.rag.timeline_reasoner import build_timeline

documents = [
    {
        "title": "Master Directions on Relief/Savings Bonds",
        "issue_date": "July 2, 2018",
        "combined_text": "Relief Savings Bonds are issued by RBI with fixed interest rates.",
        "document_type": "MASTER_DIRECTION",
        "department": "DBR",
        "source": "RBI"
    },
    {
        "title": "Master Circular on Relief Bonds",
        "issue_date": "April 1, 2022",
        "combined_text": "This circular amends certain provisions of earlier directions.",
        "document_type": "MASTER_CIRCULAR",
        "department": "DBR",
        "source": "RBI"
    }
]

timeline = build_timeline(documents)

result = generate_timeline_answer(
    question="How have Relief Savings Bond rules evolved?",
    timeline_docs=timeline
)

print("\n===== TIMELINE RAG PROMPT =====\n")
print(result["prompt"])

print("\n----- SOURCES -----")
for s in result["sources"]:
    print("-", s)
