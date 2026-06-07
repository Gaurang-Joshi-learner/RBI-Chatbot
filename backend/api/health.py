from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "status": "OK",
        "service": "RBI Chatbot Backend"
    }
