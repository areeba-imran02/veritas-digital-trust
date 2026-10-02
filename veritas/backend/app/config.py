"""Central configuration. All settings come from environment variables (see .env.example).

The Groq API key is read ONLY from GROQ_API_KEY. It is never hardcoded, logged, or returned by any endpoint.
"""
from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # Secrets
    groq_api_key: SecretStr | None = None

    # Groq models
    groq_model: str = "llama-3.3-70b-versatile"
    groq_vision_model: str = "meta-llama/llama-4-scout-17b-16e-instruct"
    groq_audio_model: str = "whisper-large-v3"
    groq_timeout_seconds: float = 30.0

    # App
    veritas_env: str = "development"
    veritas_log_level: str = "INFO"
    veritas_default_locale: str = "en"
    veritas_max_upload_mb: int = 10
    veritas_cors_origins: str = "http://localhost:5173"
    veritas_static_dir: str = "../frontend/dist"

    @property
    def llm_configured(self) -> bool:
        return bool(self.groq_api_key and self.groq_api_key.get_secret_value().strip())

    @property
    def cors_origins(self) -> list[str]:
        return [o.strip() for o in self.veritas_cors_origins.split(",") if o.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
