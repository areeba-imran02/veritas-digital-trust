"""VERITAS application entrypoint. Run: uvicorn app.main:app --reload (from /backend)."""
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app import __version__
from app.api.router import api_router
from app.config import get_settings


def create_app() -> FastAPI:
    s = get_settings()
    app = FastAPI(title="VERITAS", version=__version__,
                  description="Digital Trust & Safety Platform. Understand. Verify. Trust.")
    app.add_middleware(CORSMiddleware, allow_origins=s.cors_origins,
                       allow_methods=["*"], allow_headers=["*"])
    app.include_router(api_router)

    # Serve the built frontend when present (production / single-container deploy).
    static_dir = Path(s.veritas_static_dir)
    if static_dir.is_dir():
        app.mount("/", StaticFiles(directory=static_dir, html=True), name="frontend")
    return app


app = create_app()
