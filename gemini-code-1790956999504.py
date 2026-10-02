import os
import json
from groq import Groq
from core.config import Config

class GroqService:
    def __init__(self):
        api_key = os.environ.get("GROQ_API_KEY")
        self.client = Groq(api_key=api_key) if api_key else None

    def query(self, system_prompt: str, user_prompt: str, temperature: float = 0.1) -> dict:
        if not self.client:
            return {"error": "Groq API key not configured. Using heuristic fallback.", "fallback": True}
        
        try:
            response = self.client.chat.completions.create(
                model=Config.DEFAULT_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=temperature,
                response_format={"type": "json_object"}
            )
            content = response.choices[0].message.content
            return json.loads(content)
        except Exception as e:
            try:
                response = self.client.chat.completions.create(
                    model=Config.FALLBACK_MODEL,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=temperature
                )
                content = response.choices[0].message.content
                return json.loads(content)
            except Exception as inner_e:
                return {"error": str(inner_e), "fallback": True}