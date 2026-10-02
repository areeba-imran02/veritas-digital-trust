class ContentAgent:
    """
    VERITAS Content Agent

    Purpose:
    Understand and structure the user's digital content
    before other agents perform deeper analysis.
    """

    def __init__(self):
        self.name = "Content Agent"

    def analyze(self, content):
        """
        Analyze the basic characteristics of the input.
        """

        if not content or not content.strip():
            return {
                "agent": self.name,
                "status": "empty",
                "content_type": "unknown",
                "content": "",
            }

        text = content.strip()

        return {
            "agent": self.name,
            "status": "analyzed",
            "content_type": self.detect_content_type(text),
            "content": text,
            "length": len(text),
        }

    def detect_content_type(self, content):
        """
        Basic content-type detection.

        More advanced multimodal detection will be added later.
        """

        lowered = content.lower()

        if lowered.startswith(("http://", "https://", "www.")):
            return "url"

        if "@" in content and "." in content:
            return "email_or_message"

        if any(
            keyword in lowered
            for keyword in [
                "urgent",
                "verify",
                "account",
                "payment",
                "click",
                "password",
                "otp",
            ]
        ):
            return "digital_message"

        return "text"
