class IdentityAgent:
    def evaluate(self, extracted_data: dict) -> dict:
        sender = extracted_data.get("sender", "")
        spoofing = False
        explanation = "Sender identifier appears consistent."
        
        if sender and ("@gmail.com" in sender or "@yahoo.com" in sender) and any(b in sender.lower() for b in ["bank", "gov", "sec", "support"]):
            spoofing = True
            explanation = "Free public email domain used while claiming official institutional authority."
            
        return {
            "sender": sender,
            "spoofing_detected": spoofing,
            "spoofing_explanation": explanation
        }
