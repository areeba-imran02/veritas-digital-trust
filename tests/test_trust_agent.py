from agents.trust_agent import TrustAgent

def test_trust_agent_verdict():
    agent = TrustAgent()
    risk_eval = {"threat_score": 0.85, "severity": "CRITICAL"}
    evidence = {"mismatch_detected": True}
    verdict = agent.issue_verdict(risk_eval, evidence)
    assert verdict == "HIGH RISK"
