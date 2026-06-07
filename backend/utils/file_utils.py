import json
from pathlib import Path
from datetime import date

SNAPSHOT_DIR = Path("app/storage/snapshots")
SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)

def save_snapshot(data: dict) -> Path:
    today = date.today().isoformat()
    file_path = SNAPSHOT_DIR / f"{today}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return file_path

def load_latest_snapshot():
    snapshots = sorted(SNAPSHOT_DIR.glob("*.json"))
    if not snapshots:
        return None
    with open(snapshots[-1], "r", encoding="utf-8") as f:
        return json.load(f)
