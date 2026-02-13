import pdfplumber
from pdfplumber.utils.exceptions import PdfminerException


def extract_text_from_pdf(pdf_path: str) -> list[dict]:
    """
    Extracts text from text-based PDFs only.
    Returns [] for scanned or invalid PDFs.
    """

    pages = []

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages, start=1):
                text = page.extract_text()
                if text and text.strip():
                    pages.append({
                        "page": i,
                        "text": text.strip()
                    })
    except (PdfminerException, Exception) as e:
        print(f"[SKIP] PDF extraction failed: {pdf_path} → {e}")
        return []

    return pages
