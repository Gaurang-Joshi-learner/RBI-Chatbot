# app/services/scraper/rbi_document_parser.py

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

HEADERS = {"User-Agent": "Mozilla/5.0"}

def parse_document_page(doc):
    url = doc["url"]
    response = requests.get(url, headers=HEADERS, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # 🔍 Look for PDF
    for a in soup.select("a[href$='.pdf']"):
        return {
            **doc,
            "content_type": "PDF",
            "pdf_url": urljoin(url, a["href"])
        }

    # 🔍 Else fallback to HTML
    content_div = soup.find("div", id="divContent") or soup.body

    text = content_div.get_text("\n", strip=True) if content_div else ""

    return {
        **doc,
        "content_type": "HTML",
        "text": text
    }
