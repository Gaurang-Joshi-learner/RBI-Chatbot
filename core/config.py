from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    PROJECT_NAME = "RBI Regulatory Chatbot"
    DATABASE_URL = os.getenv("DATABASE_URL")

settings = Settings()
