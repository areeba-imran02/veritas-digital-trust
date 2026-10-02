import os

class Config:
    VERSION = "4.2.0-Enterprise"
    DEFAULT_MODEL = "llama3-70b-8192"
    FALLBACK_MODEL = "llama3-8b-8192"
    SUPPORTED_LANGUAGES = ["English", "Urdu (اردو)", "Roman Urdu"]
    REGION_TAG = "PK"
    
    @staticmethod
    get_groq_key = lambda: os.environ.get("GROQ_API_KEY", "")