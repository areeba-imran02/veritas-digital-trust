import os

class Config:
    VERSION = "4.2.0-Enterprise"
    DEFAULT_MODEL = "openai/gpt-oss-120b"
    FALLBACK_MODEL = "openai/gpt-oss-120b"
    SUPPORTED_LANGUAGES = ["English", "Urdu (اردو)", "Roman Urdu"]
    REGION_TAG = "PK"
    
    @staticmethod
    def get_groq_key():
        return os.environ.get("GROQ_API_KEY", "")
