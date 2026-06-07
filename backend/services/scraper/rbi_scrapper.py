# app/services/scraper/rbi_scrapper.py

from datetime import date
from typing import Dict, Any

from app.utils.hash_utils import generate_doc_id
from app.services.scraper.rbi_seed_scraper import scrape_seed_pages
from app.services.scraper.rbi_document_parser import parse_document_page


def scrape_rbi(limit: int | None = None) -> Dict[str, Any]:
    """
    Main RBI scraper.
    Returns a SNAPSHOT in canonical format:

    {
        run_date: str,
        source: "RBI",
        documents: {
            doc_id: { ...document data... }
        }
    }
    """

    seeds = scrape_seed_pages()
    documents: Dict[str, Dict] = {}

    if limit:
        seeds = seeds[:limit]

    for seed in seeds:
        try:
            parsed = parse_document_page(seed)

            # ✅ Stable document ID (VERY IMPORTANT)
            doc_id = generate_doc_id(
                parsed.get("title", ""),
                parsed.get("url", "")
            )

            parsed["doc_id"] = doc_id
            parsed["source"] = "RBI"

            documents[doc_id] = parsed

        except Exception as e:
            # Never crash scraper for one bad page
            print(f"[SKIP] Failed parsing {seed.get('url')} → {e}")

    snapshot = {
        "run_date": date.today().isoformat(),
        "source": "RBI",
        "documents": documents
    }

    return snapshot
