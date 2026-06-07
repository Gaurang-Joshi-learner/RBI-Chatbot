from app.services.scraper.rbi_scrapper import scrape_rbi

def run_scraper(limit: int | None = None):
    print(">>> SCRAPER RUNNER STARTED")

    snapshot = scrape_rbi(limit=limit)

    print(">>> SCRAPER RUNNER FINISHED")
    print(">>> Documents:", len(snapshot.get("documents", {})))

    return snapshot
