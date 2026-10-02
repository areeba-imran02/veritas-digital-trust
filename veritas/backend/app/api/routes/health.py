from fastapi import APIRouter

from app import __version__
from app.config import get_settings

router = APIRouter(tags=["system"])


@router.get("/health")
def health() -> dict:
    s = get_settings()
    return {
        "status": "ok",
        "service": "veritas",
        "version": __version__,
        "environment": s.veritas_env,
        "llm_configured": s.llm_configured,  # boolean only; the key itself is never exposed
    }
