from fastapi import Header, HTTPException, Depends
import os

ADMIN_API_KEY = os.getenv("ADMIN_API_KEY")  # later move this to env variable

def verify_admin_key(x_api_key: str = Header(None)):
    if x_api_key != ADMIN_API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden: Invalid API Key")
