import re
from urllib.parse import urlparse

class URLAnalyzer:
    def analyze(self, url: str) -> dict:
        if not url:
            return {"valid": False}
        
        parsed = urlparse(url if "://" in url else "http://" + url)
        domain = parsed.netloc or parsed.path
        
        shorteners = ["bit.ly", "tinyurl.com", "t.co", "goo.gl", "ow.ly", "rb.gy"]
        is_shortener = any(s in domain.lower() for s in shorteners)
        
        suspicious_keywords = ["verify", "login", "update", "bank", "secure", "account", "prize", "winner"]
        has_suspicious_keyword = any(kw in domain.lower() for kw in suspicious_keywords)
        
        has_https = parsed.scheme == "https"
        
        is_suspicious = is_shortener or (has_suspicious_keyword and not has_https) or len(domain.split('.')) > 4
        
        return {
            "url": url,
            "domain": domain,
            "is_shortener": is_shortener,
            "has_https": has_https,
            "has_suspicious_keyword": has_suspicious_keyword,
            "is_suspicious": is_suspicious
        }