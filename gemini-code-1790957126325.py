from analyzers.qr_analyzer import QRAnalyzer

def test_qr_analyzer_fallback():
    analyzer = QRAnalyzer()
    res = analyzer.analyze(None)
    assert res["decoded"] is False