from app.config import Settings


def test_no_key_by_default(monkeypatch):
    monkeypatch.delenv("GROQ_API_KEY", raising=False)
    assert Settings(_env_file=None).llm_configured is False


def test_key_from_env(monkeypatch):
    monkeypatch.setenv("GROQ_API_KEY", "test-value")
    s = Settings(_env_file=None)
    assert s.llm_configured is True
    assert "test-value" not in repr(s)  # SecretStr hides it
