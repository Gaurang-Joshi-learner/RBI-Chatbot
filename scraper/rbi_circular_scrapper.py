# app/services/scrapper/rbi_circular_scrapper.py
import requests
from bs4 import BeautifulSoup
from datetime import date
from urllib.parse import urljoin

from app.utils.hash_utils import generate_doc_id

BASE_URL = "https://www.rbi.org.in"
CIRCULAR_URL = "https://www.rbi.org.in/Scripts/BS_ViewMasCirculardetails.aspx"

def scrape_rbi_circulars():
    response = requests.get(CIRCULAR_URL, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    documents = {}

    # Anchor-based scraping (stable)
    links = soup.select('a[href*="BS_CircularIndexDisplay.aspx"]')

    for link in links:
        title = link.get_text(strip=True)
        href = link.get("href")

        if not title or not href:
            continue

        url = urljoin(BASE_URL, href)
        doc_id = generate_doc_id(title, url)

        documents[doc_id] = {
            "title": title,
            "type": "CIRCULAR",
            "source": "RBI",
            "url": url
        }

    return {
        "run_date": date.today().isoformat(),
        "source": "RBI_CIRCULAR",
        "documents": documents
    }
