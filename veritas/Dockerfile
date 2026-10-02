# VERITAS - single-container build: frontend is built, then served by the FastAPI backend.

# ---- Stage 1: build frontend ----
FROM node:20-alpine AS frontend-build
WORKDIR /frontend
COPY frontend/package.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# ---- Stage 2: runtime ----
FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /srv
COPY backend/requirements.txt backend/requirements.txt
RUN pip install --no-cache-dir -r backend/requirements.txt
COPY backend/ backend/
COPY --from=frontend-build /frontend/dist frontend/dist
ENV VERITAS_STATIC_DIR=/srv/frontend/dist VERITAS_ENV=production
WORKDIR /srv/backend
# GROQ_API_KEY must be provided by the deployment platform as a secret.
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
