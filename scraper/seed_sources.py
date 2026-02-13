# app/services/scraper/seed_sources.py

RBI_SEED_URLS = {
    "notifications": {
        "url": "https://www.rbi.org.in/Scripts/NotificationUser.aspx",
        "content_type": "NOTIFICATION",
    },
    "master_directions": {
        "url": "https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx",
        "content_type": "MASTER_DIRECTION",
    },
    "master_circulars": {
        "url": "https://www.rbi.org.in/Scripts/BS_ViewMasterCirculars.aspx",
        "content_type": "MASTER_CIRCULAR",
    },
}
