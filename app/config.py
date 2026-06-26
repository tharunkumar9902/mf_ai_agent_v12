import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL")

MF_API_BASE_URL = os.getenv("MF_API_BASE_URL", "https://api.mfapi.in/mf")
MF_SEARCH_URL = os.getenv("MF_SEARCH_URL", "https://api.mfapi.in/mf/search")
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is missing")
