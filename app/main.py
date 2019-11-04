import json
from fastapi import FastAPI
from SentimentAnalysis.sentiment_main import SentimentAnalysis

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Data Enricher"}

@app.get('/sentiment/{sentiment_text}')
def sentiment_analysis(sentiment_text):
	sentAnalysis = SentimentAnalysis(sentiment_text)
	return sentAnalysis.get_sentiment_analysis()

@app.get('/sentiment-polarity/{sentiment_text}')
def polarity_score(sentiment_text):
	sentAnalysis = SentimentAnalysis(sentiment_text)
	return sentAnalysis.get_polarity_score()

@app.get('/sentiment-subjectivity/{sentiment_text}')
def subjectivity_score(sentiment_text):
	sentAnalysis = SentimentAnalysis(sentiment_text)
	return sentAnalysis.get_subjectivity_score()
