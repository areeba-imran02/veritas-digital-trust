class TrustAgent:
    def issue_verdict(self, risk_evaluation: dict, evidence_correlation: dict) -> str:
        score = risk_evaluation.get("threat_score", 0.0)
        
        if score >= 0.7:
            return "HIGH RISK"
        elif score >= 0.4:
            return "NEEDS VERIFICATION"
        elif score >= 0.2:
            return "LOW RISK"
        else:
            return "INSUFFICIENT EVIDENCE"