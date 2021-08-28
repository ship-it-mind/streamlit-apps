import textrazor


class TextAnalyzer:
    def __init__(self):
        textrazor.api_key = "66eade0e651a0f2bcebc886be1bf3ee02a3641f203689e0c8c758dfc"
        self.client = textrazor.TextRazor(extractors=["entities"])

    def analyze(self, text, is_url):
        if is_url:
            response = self.client.analyze_url(text)
        else:
            response = self.client.analyze(text)
        return response
