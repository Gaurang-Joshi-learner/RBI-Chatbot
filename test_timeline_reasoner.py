from app.services.rag.timeline_reasoner import build_timeline

documents = [
    {
        "title": "Master Directions on Relief/Savings Bonds",
        "issue_date": "July 2, 2018",
        "combined_text": "Relief Savings Bonds are issued by RBI."
    },
    {
        "title": "Master Circular on Relief Bonds",
        "issue_date": "April 1, 2022",
        "combined_text": "This circular is issued in partial modification of earlier directions."
    }
]

timeline = build_timeline(documents)

print("\n📅 TIMELINE OUTPUT")
print("-" * 40)

for doc in timeline:
    print(f"Title: {doc['title']}")
    print(f"Issue Date: {doc['issue_date']}")
    print(f"Relationships: {doc['relationships']}")
    print()
