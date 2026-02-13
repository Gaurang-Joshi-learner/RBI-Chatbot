# app/services/scrapper/pdf_downloader.py

from app.utils.pdf_utils import download_pdf


def download_master_pdfs(scraped_data: dict) -> dict:
    """
    Downloads PDFs for RBI master documents and updates metadata.
    """

    documents = scraped_data.get("documents", {})

    for doc_id, doc in documents.items():
        pdf_url = doc.get("url")

        if not pdf_url:
            continue

        if not pdf_url.lower().endswith(".pdf"):
            continue

        pdf_path, pdf_hash = download_pdf(pdf_url, doc_id)

        if not pdf_path:
            print(f"[SKIP] PDF not downloaded: {doc.get('title')}")
            continue

        doc["pdf_path"] = pdf_path
        doc["pdf_hash"] = pdf_hash

    return scraped_data
