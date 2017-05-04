from common.globalLogger import GlobalLogger

class ToneAnalyzer:
    def __init__(self, transcriptions, toneAnalyzer, **kwargs):
        self.tone_analyzer = toneAnalyzer()
        self.logger = GlobalLogger
        self.transcriptions = transcriptions


    def analyze(self, text):
        return self.tone_analyzer.analyze(text)