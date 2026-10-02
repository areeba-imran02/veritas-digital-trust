from analyzers.url_analyzer import URLAnalyzer
from analyzers.qr_analyzer import QRAnalyzer
from analyzers.image_analyzer import ImageAnalyzer
from analyzers.screenshot_analyzer import ScreenshotAnalyzer
from analyzers.audio_analyzer import AudioAnalyzer

from agents.content_agent import ContentAgent
from agents.identity_agent import IdentityAgent
from agents.risk_agent import RiskAgent
from agents.evidence_agent import EvidenceAgent
from agents.trust_agent import TrustAgent
from agents.action_agent import ActionAgent
from services.evidence_service import EvidenceService

class Orchestrator:
    def __init__(self):
        self.url_analyzer = URLAnalyzer()
        self.qr_analyzer = QRAnalyzer()
        self.image_analyzer = ImageAnalyzer()
        self.screenshot_analyzer = ScreenshotAnalyzer()
        self.audio_analyzer = AudioAnalyzer()

        self.content_agent = ContentAgent()
        self.identity_agent = IdentityAgent()
        self.risk_agent = RiskAgent()
        self.evidence_agent = EvidenceAgent()
        self.trust_agent = TrustAgent()
        self.action_agent = ActionAgent()
        self.evidence_service = EvidenceService()

    def analyze(self, payload: dict) -> dict:
        artifact_type = payload.get("type")
        extracted_data = {}

        # 1. Analyzer Phase
        if artifact_type == "text":
            extracted_data["content"] = payload.get("content")
            extracted_data["sender"] = payload.get("sender")
        elif artifact_type == "url":
            extracted_data["url_analysis"] = self.url_analyzer.analyze(payload.get("url"))
        elif artifact_type == "qr":
            extracted_data["qr_analysis"] = self.qr_analyzer.analyze(payload.get("file"))
        elif artifact_type == "screenshot":
            extracted_data["screenshot_analysis"] = self.screenshot_analyzer.analyze(payload.get("file"))
        elif artifact_type == "audio":
            extracted_data["audio_analysis"] = self.audio_analyzer.analyze(payload.get("file"))
        else:
            extracted_data["content"] = str(payload)

        # 2. Multi-Agent Intelligence Phase
        content_findings = self.content_agent.evaluate(extracted_data)
        identity_findings = self.identity_agent.evaluate(extracted_data)
        evidence_correlation = self.evidence_agent.correlate(extracted_data, content_findings, identity_findings)
        
        risk_evaluation = self.risk_agent.compute_risk(content_findings, identity_findings, evidence_correlation)
        trust_verdict = self.trust_agent.issue_verdict(risk_evaluation, evidence_correlation)
        action_plan = self.action_agent.formulate_plan(trust_verdict, risk_evaluation, evidence_correlation)

        # 3. Evidence Packaging
        evidence_cards = self.evidence_service.build_cards(extracted_data, content_findings, identity_findings)

        return {
            "artifact_type": artifact_type,
            "extracted_data": extracted_data,
            "content_findings": content_findings,
            "identity_findings": identity_findings,
            "evidence_correlation": evidence_correlation,
            "risk_evaluation": risk_evaluation,
            "trust_verdict": trust_verdict,
            "action_plan": action_plan,
            "evidence_cards": evidence_cards
        }