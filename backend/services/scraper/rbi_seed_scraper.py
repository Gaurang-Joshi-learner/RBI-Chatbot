import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from app.services.scraper.seed_sources import RBI_SEED_URLS

HEADERS = {"User-Agent": "Mozilla/5.0"}


def scrape_seed_pages():
    """
    Crawls RBI seed pages and returns document landing pages (HTML/PDF links)
    """
    documents = []

    for category, cfg in RBI_SEED_URLS.items():
        seed_url = cfg["url"]
        content_type = cfg["content_type"]

        response = requests.get(seed_url, headers=HEADERS, timeout=20)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for a in soup.select("a[href]"):
            href = a.get("href")
            title = a.get_text(strip=True)

            if not title or not href:
                continue

            if any(k in href for k in [
                "Notification.aspx",
                "BS_ViewMasDirections.aspx",
                "BS_ViewMasterCirculars.aspx",
                ".PDF",
                ".pdf"
            ]):
                documents.append({
                    "title": title,
                    "url": urljoin(seed_url, href),
                    "category": category,
                    "content_type": content_type,
                })

    return documents
