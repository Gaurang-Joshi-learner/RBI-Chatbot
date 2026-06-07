import requests
from bs4 import BeautifulSoup
from datetime import date
from urllib.parse import urljoin

from app.utils.hash_utils import generate_doc_id

BASE_URL = "https://www.rbi.org.in"

MASTER_SOURCES = {
    "MASTER_CIRCULAR": "https://www.rbi.org.in/Scripts/BS_ViewMasCircul.aspx",
    "MASTER_DIRECTION": "https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx",
}


def scrape_rbi_master_directions():
    """
    Scrapes RBI Master Circulars and Master Directions (HTML pages only).
    """

    all_documents = {}

    for doc_type, url in MASTER_SOURCES.items():
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        rows = soup.select("table tr")[1:]  # skip header

        for row in rows:
            cols = row.find_all("td")
            if len(cols) < 2:
                continue

            title = cols[1].get_text(strip=True)
            link = cols[1].find("a")

            if not title or not link or not link.get("href"):
                continue

            doc_url = urljoin(BASE_URL, link["href"])
            doc_id = generate_doc_id(title, doc_url)

            all_documents[doc_id] = {
                "doc_id": doc_id,
                "title": title,
                "document_type": doc_type,
                "source": "RBI",
                "url": doc_url,
            }

    return {
        "run_date": date.today().isoformat(),
        "source": "RBI_MASTER",
        "total_documents": len(all_documents),
        "documents": all_documents,
    }
