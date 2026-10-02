from agents.identity_agent import IdentityAgent

def test_identity_agent_evaluation():
    agent = IdentityAgent()
    sample_data = {"sender": "support@gmail.com"}
    result = agent.evaluate(sample_data)
    assert result["spoofing_detected"] is True