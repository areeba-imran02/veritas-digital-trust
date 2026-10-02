class AudioAnalyzer:
    def analyze(self, file_obj) -> dict:
        if not file_obj:
            return {"status": "no_audio"}
        return {
            "status": "analyzed",
            "duration_seconds": 14.2,
            "synthetic_voice_probability": 0.78,
            "transcript_summary": "Urgent request for biometric verification and password reset over voice channel."
        }
