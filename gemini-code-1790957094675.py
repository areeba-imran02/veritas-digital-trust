class ActionAgent:
    def formulate_plan(self, verdict: str, risk_evaluation: dict, evidence_correlation: dict) -> dict:
        if verdict == "HIGH RISK":
            why = "Multiple high-severity threat indicators identified, including psychological manipulation and potential sender spoofing."
            steps = [
                "Do not click any links, scan QR codes, or reply to the message.",
                "Block the sender identifier immediately across all communication channels.",
                "Report the artifact to internal security operations or national cybercrime authorities."
            ]
        elif verdict == "NEEDS VERIFICATION":
            why = "Ambiguous threat signatures detected that require out-of-band confirmation."
            steps = [
                "Verify the request independently by calling official customer support using a trusted number.",
                "Do not share personal credentials, OTPs, or financial information.",
                "Monitor accounts for unusual activity."
            ]
        else:
            why = "Artifact exhibits normal operational patterns with no acute threat signatures."
            steps = [
                "Standard operational hygiene applies.",
                "Proceed with caution and maintain baseline verification protocols."
            ]
            
        return {
            "reasoning_why": why,
            "action_checklist": steps
        }