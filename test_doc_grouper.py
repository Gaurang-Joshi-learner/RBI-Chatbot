# test_doc_grouper.py

from app.services.rag.doc_grouper import group_chunks_by_document


def test_doc_grouper():
    retrieved_chunks = [
        {
            "text": "Relief Savings Bonds are issued by RBI.",
            "metadata": {
                "title": "Master Directions on Relief/Savings Bonds",
                "issue_date": "July 2, 2018",
                "document_type": "MASTER_DIRECTION",
                "department": "DBR",
                "source": "RBI",
                "url": "https://www.rbi.org.in/example1",
            },
        },
        {
            "text": "These bonds have fixed interest rates.",
            "metadata": {
                "title": "Master Directions on Relief/Savings Bonds",
                "issue_date": "July 2, 2018",
                "document_type": "MASTER_DIRECTION",
                "department": "DBR",
                "source": "RBI",
                "url": "https://www.rbi.org.in/example1",
            },
        },
        {
            "text": "NBFCs must comply with RBI regulations.",
            "metadata": {
                "title": "Master Circular on NBFCs",
                "issue_date": "April 1, 2022",
                "document_type": "MASTER_CIRCULAR",
                "department": "DNBR",
                "source": "RBI",
                "url": "https://www.rbi.org.in/example2",
            },
        },
    ]

    documents = group_chunks_by_document(retrieved_chunks)

    print("\n📦 GROUPED DOCUMENTS OUTPUT")
    print("----------------------------------")

    for i, doc in enumerate(documents, start=1):
        print(f"\n📄 Document {i}")
        print(f"Title       : {doc['title']}")
        print(f"Issue Date  : {doc['issue_date']}")
        print(f"Type        : {doc['document_type']}")
        print(f"Department  : {doc['department']}")
        print(f"Source      : {doc['source']}")
        print(f"Chunks      : {len(doc['chunks'])}")
        print("\nCombined Text:\n")
        print(doc["combined_text"])
        print("----------------------------------")


if __name__ == "__main__":
    test_doc_grouper()
