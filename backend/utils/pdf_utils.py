# app/utils/pdf_utils.py

import os
import requests
import hashlib

PDF_DIR = "storage/pdfs/rbi"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    ),
    "Accept": "application/pdf",
}


def download_pdf(url: str, doc_id: str):
    os.makedirs(PDF_DIR, exist_ok=True)
    path = os.path.join(PDF_DIR, f"{doc_id}.pdf")

    # Avoid re-download
    if os.path.exists(path):
        return path, compute_hash(path)

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=40,
            allow_redirects=True
        )
        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "").lower()
        if "pdf" not in content_type and "octet-stream" not in content_type:
            print(f"[SKIP] Not a PDF → {url} ({content_type})")
            return None, None

        with open(path, "wb") as f:
            f.write(response.content)

        print(f"[OK] PDF downloaded → {path}")
        return path, compute_hash(path)

    except Exception as e:
        print(f"[ERROR] PDF download failed → {url}\n{e}")
        return None, None


def compute_hash(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()
