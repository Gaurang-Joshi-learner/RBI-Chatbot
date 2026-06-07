import hashlib


def generate_doc_id(title: str, pdf_url: str) -> str:
    """
    Stable document ID based on title + URL.
    """
    raw = f"{title}|{pdf_url}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:16]
