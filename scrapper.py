# app/api/scraper.py

from fastapi import APIRouter
from app.services.scraper.scraper_runner import run_scraper
from app.services.scraper.change_detector import detect_changes
from app.utils.file_utils import save_snapshot, load_latest_snapshot
from fastapi import APIRouter, Depends
from app.core.security import verify_admin_key


router = APIRouter(prefix="/scraper", tags=["Scraper"])


@router.post("/run",dependencies=[Depends(verify_admin_key)])
def run_scraper_api():
    previous_snapshot = load_latest_snapshot()

    # ✅ MUST return a snapshot dict
    current_snapshot = run_scraper()

    changes = detect_changes(previous_snapshot, current_snapshot)
    snapshot_path = save_snapshot(current_snapshot)

    return {
        "snapshot_saved": str(snapshot_path),
        "changes_detected": changes
    }
