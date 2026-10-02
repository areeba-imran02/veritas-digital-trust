class RiskAgent:
    def compute_risk(self, content_findings: dict, identity_findings: dict, evidence_correlation: dict) -> dict:
        score = 0.2
        if content_findings.get("urgency_detected"):
            score += 0.4
        if identity_findings.get("spoofing_detected"):
            score += 0.3
        if evidence_correlation.get("mismatch_detected"):
            score += 0.1
            
        score = min(score, 1.0)
        
        if score >= 0.75:
            severity = "CRITICAL"
        elif score >= 0.5:
            severity = "HIGH"
        elif score >= 0.3:
            severity = "MEDIUM"
        else:
            severity = "LOW"
            
        return {
            "threat_score": round(score, 2),
            "severity": severity
        }