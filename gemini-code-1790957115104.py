from agents.content_agent import ContentAgent

def test_content_agent_evaluation():
    agent = ContentAgent()
    sample_data = {"content": "Urgent alert: your bank account is blocked. Click here immediately."}
    result = agent.evaluate(sample_data)
    assert isinstance(result, dict)
    assert "urgency_detected" in result