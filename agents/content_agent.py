from services.groq_service import GroqService

class ContentAgent:
    def __init__(self):
        self.groq = GroqService()

    def evaluate(self, extracted_data: dict) -> dict:
        content = extracted_data.get("content") or extracted_data.get("screenshot_analysis", {}).get("ocr_text_extracted") or ""
        content_lower = content.lower()
        
        prompt = f"""
        Analyze the following message content for psychological manipulation, urgency triggers, fake authority, and financial scam signatures.
        Return a JSON object with keys:
        - "urgency_detected": boolean
        - "urgency_explanation": string
        - "manipulation_score": float between 0.0 and 1.0
        - "signatures": list of strings
        
        Content: "{content}"
        """
        
        # Try querying Groq API
        result = self.groq.query("You are an expert cybersecurity content analysis agent. Return valid JSON only.", prompt)
        
        # If Groq fails, return a smart dynamic heuristic analysis based strictly on actual input text
        if not isinstance(result, dict) or "error" in result or not result:
            if not content.strip():
                return {
                    "urgency_detected": False,
                    "urgency_explanation": "No text content provided for analysis.",
                    "manipulation_score": 0.0,
                    "signatures": ["None"]
                }
            
            # Dynamic keyword inspection on actual input text
            urgent_keywords = ["urgent", "immediately", "block", "suspended", "verify", "expire", "winner", "prize", "atm", "pin", "password", "click", "jazzcash", "easypaisa"]
            matched_keywords = [kw for kw in urgent_keywords if kw in content_lower]
            is_urgent = len(matched_keywords) > 0
            
            signatures = []
            if any(w in content_lower for w in ["block", "suspended", "locked"]):
                signatures.append("Account restriction / freezing threat detected")
            if any(w in content_lower for w in ["verify", "click", "link", "update", "login"]):
                signatures.append("Credential harvesting / Phishing link request")
            if any(w in content_lower for w in ["winner", "prize", "congratulations", "cash"]):
                signatures.append("Lottery / Financial scam trap indicator")
            
            if not signatures and is_urgent:
                signatures.append("High-pressure psychological trigger words found")
            if not signatures:
                signatures.append("Standard conversational or safe informational text (Low Risk)")
            
            # Dynamic score calculation based on actual input
            score = min(0.9, 0.15 + (len(matched_keywords) * 0.25)) if is_urgent else 0.05
            explanation = f"Dynamic text analysis completed. Identified {len(matched_keywords)} risk indicator(s) in your input: {', '.join(matched_keywords) if matched_keywords else 'None'}."
            
            return {
                "urgency_detected": is_urgent,
                "urgency_explanation": explanation,
                "manipulation_score": round(score, 2),
                "signatures": signatures
            }
            
        return result
