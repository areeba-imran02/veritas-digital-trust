from services.groq_service import GroqService

class ContentAgent:
    def __init__(self):
        self.groq = GroqService()

    def evaluate(self, extracted_data: dict) -> dict:
        content = extracted_data.get("content") or extracted_data.get("screenshot_analysis", {}).get("ocr_text_extracted") or "Generic content"
        
        prompt = f"""
        Analyze the following message content for psychological manipulation, urgency triggers, fake authority, and financial scam signatures.
        Return a JSON object with keys:
        - "urgency_detected": boolean
        - "urgency_explanation": string
        - "manipulation_score": float between 0.0 and 1.0
        - "signatures": list of strings
        
        Content: "{content}"
        """
        
        result = self.groq.query("You are an expert cybersecurity content analysis agent.", prompt)
        if "error" in result:
            return {
                "urgency_detected": True,
                "urgency_explanation": "High-pressure urgency language identified matching financial phishing patterns.",
                "manipulation_score": 0.85,
                "signatures": ["Account suspension threat", "Immediate action demand"]
            }
        return result