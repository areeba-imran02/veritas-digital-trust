class ImageAnalyzer:
    def analyze(self, file_obj) -> dict:
        if not file_obj:
            return {"status": "no_image"}
        return {
            "status": "analyzed",
            "filename": getattr(file_obj, "name", "uploaded_image.png"),
            "visual_anomalies": False,
            "ocr_text_extracted": "Sample OCR extraction from visual artifact: Account Verification Notice."
        }
