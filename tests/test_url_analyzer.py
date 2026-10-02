from analyzers.url_analyzer import URLAnalyzer

def test_url_analyzer_suspicious():
    analyzer = URLAnalyzer()
    res = analyzer.analyze("https://bit.ly/fake-bank-login")
    assert res["is_shortener"] is True
    assert res["is_suspicious"] is True
