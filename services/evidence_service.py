class EvidenceService:
    def build_cards(self, extracted_data: dict, content_findings: dict, identity_findings: dict) -> list:
        cards = []
        if "url_analysis" in extracted_data:
            ua = extracted_data["url_analysis"]
            cards.append({
                "title": "URL Threat Inspection",
                "severity": "High" if ua.get("is_suspicious") else "Low",
                "details": f"Domain: {ua.get('domain', 'Unknown')} | Shortener: {ua.get('is_shortener', False)} | HTTPS: {ua.get('has_https', True)}"
            })
        if "qr_analysis" in extracted_data:
            qa = extracted_data["qr_analysis"]
            cards.append({
                "title": "QR Payload Analysis",
                "severity": "Medium" if qa.get("decoded_data") else "Low",
                "details": f"Payload Extracted: {qa.get('decoded_data', 'None')}"
            })
        if content_findings.get("urgency_detected"):
            cards.append({
                "title": "Psychological Urgency Trigger",
                "severity": "High",
                "details": content_findings.get("urgency_explanation", "High-pressure tactics identified in text.")
            })
        if identity_findings.get("spoofing_detected"):
            cards.append({
                "title": "Identity Imposter Indicator",
                "severity": "High",
                "details": identity_findings.get("spoofing_explanation", "Sender mismatch or domain spoofing detected.")
            })
        if not cards:
            cards.append({
                "title": "Standard Artifact Review",
                "severity": "Low",
                "details": "No acute anomalies or high-risk signatures flagged in preliminary scan."
            })
        return cards
