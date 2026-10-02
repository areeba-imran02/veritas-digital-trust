from core.orchestrator import Orchestrator

def test_orchestrator_pipeline():
    orch = Orchestrator()
    payload = {"type": "text", "content": "Test scam message", "sender": "test@test.com"}
    res = orch.analyze(payload)
    assert "trust_verdict" in res
    assert "action_plan" in res
    assert "evidence_cards" in res
