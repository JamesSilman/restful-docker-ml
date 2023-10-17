import json
from textblob import TextBlob

class SentimentAnalysis:

	sentiment_text = ""
	analysis = ()
	polarity_score = 0
	subjectivity_score = 0

	def __init__(self, sentiment_text):
		self.sentiment_text = sentiment_text
		self.run_sentiment_analysis()
		
	def run_sentiment_analysis(self):
		self.analysis = TextBlob(self.sentiment_text)
		
	def get_sentiment_analysis(self):
		return {
				"polarity": json.dumps(self.analysis.sentiment.polarity),
				"subjectivity": json.dumps(self.analysis.sentiment.subjectivity)
				}

	def get_polarity_score(self):
		return {"polarity_score": json.dumps(self.analysis.sentiment.polarity)}

	def get_subjectivity_score(self):
		return {"subjectivity_score": json.dumps(self.analysis.sentiment.subjectivity)}
