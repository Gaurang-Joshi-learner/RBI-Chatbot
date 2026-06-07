from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware   # ✅ ADD THIS

# -----------------------------
# Existing imports
# -----------------------------
from app.core.config import settings
from app.api.health import router as health_router
from app.db.session import engine
from app.db.base import Base
from app.api.debug import router as debug_router
from app.api.ask import router as ask_router
from app.api.scrapper import router as scrapper_router
from app.db.session import engine, Base
from app.models.chat import ChatSession, Message
from app.api.sessions import router as sessions_router
from app.models.user import User
from app.api.auth import router as auth_router

# -----------------------------
# Create DB tables
# -----------------------------
Base.metadata.create_all(bind=engine)

# -----------------------------
# FastAPI app
# -----------------------------
app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0"
)

# -----------------------------
# ✅ CORS MIDDLEWARE (THIS FIXES FRONTEND)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[ "http://localhost:5173",],   # allow all for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Routers
# -----------------------------
app.include_router(health_router)
app.include_router(debug_router)
app.include_router(ask_router)
app.include_router(scrapper_router)
app.include_router(sessions_router)
app.include_router(auth_router)
# -----------------------------
# Root endpoint
# -----------------------------
@app.get("/")
def root():
    return {"message": "RBI Regulatory Chatbot API is running"}
