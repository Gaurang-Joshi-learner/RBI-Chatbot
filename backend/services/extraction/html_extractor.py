# app/services/extraction/html_extractor.py

import requests
from bs4 import BeautifulSoup
from typing import Dict

HEADERS = {"User-Agent": "Mozilla/5.0"}


def extract_rbi_html_text(url: str) -> Dict:
    response = requests.get(url, headers=HEADERS, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.get_text(strip=True) if soup.title else "RBI Document"

    # ❌ RBI error page detection
    if "Sorry for your inconvenience" in soup.get_text():
        raise ValueError("RBI error page detected")

    # ✅ Step 1: Try known RBI containers
    container_candidates = [
        {"id": "divContent"},
        {"id": "content"},
        {"id": "innerContent"},
        {"class": "main-content"},
    ]

    content_block = None

    for selector in container_candidates:
        content_block = soup.find("div", selector)
        if content_block:
            break

    # ✅ Step 2: Try article / table (used in many RBI pages)
    if not content_block:
        content_block = soup.find("article")

    if not content_block:
        tables = soup.find_all("table")
        if tables:
            content_block = max(tables, key=lambda t: len(t.get_text()))

    # ✅ Step 3: Smart fallback (last resort)
    if not content_block:
        body = soup.body
        if not body:
            raise ValueError("No usable content found")

        # Remove nav/header/footer
        for tag in body.find_all(["nav", "header", "footer", "aside"]):
            tag.decompose()

        content_block = body

    # 🧹 Cleanup scripts & styles
    for tag in content_block(["script", "style", "noscript"]):
        tag.decompose()

    raw_text = content_block.get_text(separator="\n", strip=True)

    # 🧹 Noise removal
    noise_phrases = [
        "Skip to main content",
        "Click here to Visit the RBI’s new website",
        "Selected Language",
        "Search the Website",
        "Back to previous page",
        "More Links",
        "Archives",
        "Bank Holidays",
        "Contact Us",
        "© Reserve Bank of India",
    ]

    cleaned_lines = []
    for line in raw_text.splitlines():
        line = line.strip()
        if len(line) < 5:
            continue
        if any(p.lower() in line.lower() for p in noise_phrases):
            continue
        cleaned_lines.append(line)

    cleaned_text = "\n".join(cleaned_lines)

    # ✅ Validation: regulation sanity check
    regulatory_markers = [
        "Reserve Bank of India",
        "RBI/",
        "Master Directions",
        "Circular",
        "Notification",
        "These directions",
        "Applicability",
        "shall come into force",
    ]

    matches = sum(1 for m in regulatory_markers if m.lower() in cleaned_text.lower())

    if matches < 2:
        raise ValueError("Extracted page is not a regulatory document")

    if len(cleaned_text) < 2000:
        raise ValueError("Extracted text too small")

    return {
        "title": title,
        "text": cleaned_text,
        "url": url,
    }
