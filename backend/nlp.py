# nlp.py
from summarizer import SummarizationModel

class NLP:
    summary = SummarizationModel()
    def summary(self, text:str, summary): 
        sentiment = summary.get_summary(text)
        return sentiment