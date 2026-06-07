from app.services.scraper.rbi_master_scrapper import scrape_rbi_master_directions
from app.services.scraper.pdf_downloader import download_master_pdfs

data = scrape_rbi_master_directions()
data = download_master_pdfs(data)

count = 0
for doc in data["documents"].values():
    if "pdf_path" in doc:
        count += 1
        print("DOWNLOADED:", doc["pdf_path"])

print("\nTOTAL PDFs DOWNLOADED:", count)
