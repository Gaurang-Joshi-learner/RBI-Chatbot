from app.services.scraper.rbi_master_scrapper import scrape_rbi_master_directions

data = scrape_rbi_master_directions()

print("RUN DATE:", data["run_date"])
print("SOURCE:", data["source"])
print("TOTAL DOCUMENTS:", data["total_documents"])
print("-" * 40)

documents = data["documents"]

for doc_id, doc in list(documents.items())[:5]:
    print("Document ID:", doc_id)
    print("TITLE:", doc["title"])
    print("DOCUMENT TYPE:", doc["document_type"])
    print("SOURCE:", doc["source"])
    print("URL:", doc["url"])
    print("-" * 40)
