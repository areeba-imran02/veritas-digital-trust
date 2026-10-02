from agents.risk_agent import RiskAgent

def test_risk_agent_computation():
    agent = RiskAgent()
    cf = {"urgency_detected": True}
    if_data = {"spoofing_detected": True}
    ec = {"mismatch_detected": False}
    result = agent.compute_risk(cf, if_data, ec)
    assert result["threat_score"] > 0.5
    assert result["severity"] in ["HIGH", "CRITICAL"]
