from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_ok_and_never_leaks_key(monkeypatch):
    r = client.get("/api/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert isinstance(body["llm_configured"], bool)
    assert "groq_api_key" not in body and "key" not in str(body).lower().replace("llm_configured", "")
