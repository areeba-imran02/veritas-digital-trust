class ScreenshotAnalyzer:
    def analyze(self, file_obj) -> dict:
        if not file_obj:
            return {"status": "no_screenshot"}
        return {
            "status": "analyzed",
            "ui_type": "messaging_chat",
            "spoofed_branding": True,
            "urgency_markers_visual": ["Immediate Action Required", "Frozen Account Warning"]
        }
