from app.services.scraper.rbi_seed_scraper import scrape_seed_pages
from app.services.scraper.rbi_document_parser import parse_document_page

docs = scrape_seed_pages()
print("Seeds:", len(docs))

sample = docs[0]
parsed = parse_document_page(sample)

print(parsed.keys())
