from app.services.scraper.rbi_master_scrapper import scrape_master_documents

print("\n===== RBI MASTER SCRAPER TEST =====\n")

result = scrape_master_documents()

print("Run Date:", result["run_date"])
print("Source:", result["source"])
print("Total documents:", result["total_documents"])

# Print first 5 docs
for i, doc in enumerate(result["documents"].values()):
    if i == 5:
        break
    print("\nTitle:", doc["title"])
    print("Type:", doc["document_type"])
    print("URL:", doc["url"])
