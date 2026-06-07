from app.services.vectorstore.indexer import index_chunks
from app.services.vectorstore.retriever import retrieve_similar_chunks

chunks = [
    {
        "chunk_id": "rbi_test_1",
        "text": "Banks must maintain Cash Reserve Ratio with RBI.",
        "doc_id": "doc123",
        "chunk_index": 0,
        "document_type": "MASTER_DIRECTION",
        "department": "DBR",
        "subject_category": "Banking Regulation",
        "issue_date": "2018-07-02",
        "source": "RBI",
        "url": "https://rbi.org.in"
    }
]

index_chunks(chunks)

results = retrieve_similar_chunks("What is CRR requirement?")
print(results)
