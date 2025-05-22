import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.0-flash")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "debug")