from app.services.scraper.rbi_scrapper import scrape_rbi
from app.services.scraper.pdf_downloader import download_master_pdfs
from app.services.vectorstore.indexer import index_all_pdfs
from app.utils.file_utils import load_latest_snapshot, save_snapshot
from app.services.scraper.change_detector import detect_changes

def run_full_ingestion_pipeline():
    print("🚀 Starting RBI ingestion pipeline...")

    # 1. Load previous snapshot
    previous_snapshot = load_latest_snapshot()

    # 2. Scrape RBI
    current_snapshot = scrape_rbi()

    # 3. Detect changes
    changes = detect_changes(previous_snapshot, current_snapshot)

    added_docs = changes["added"]
    print(f"🆕 New documents found: {len(added_docs)}")

    if not added_docs:
        print("✅ No new documents. Exiting.")
        return {"status": "no_change"}

    # 4. Download PDFs (only new ones)
    download_result = download_master_pdfs({
        "documents": {d["doc_id"]: d for d in added_docs}
    })

    print("📥 Download result:", download_result)

    # 5. Index ALL PDFs (deduplication already handled internally)
    index_result = index_all_pdfs()

    print("📚 Index result:", index_result)

    # 6. Save snapshot
    save_snapshot(current_snapshot)

    print("✅ Pipeline completed.")

    return {
        "status": "success",
        "new_docs": len(added_docs),
        "indexed": index_result
    }
