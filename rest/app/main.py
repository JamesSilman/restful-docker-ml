import json
from fastapi import FastAPI, File, UploadFile

from SentimentAnalysis.sentiment_main import SentimentAnalysis
from IPAddress.ip_address_main import IPAddress
from FacialCount.facial_count_main import FacialCount
from FacialRecognition.facial_recognition_main import FacialRecognition

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Data Enricher"}

@app.get('/sentiment/{sentiment_text}')
async def sentiment_analysis(sentiment_text):
	sentAnalysis = SentimentAnalysis(sentiment_text)
	return sentAnalysis.get_sentiment_analysis()

@app.get('/sentiment-polarity/{sentiment_text}')
async def polarity_score(sentiment_text):
	sentAnalysis = SentimentAnalysis(sentiment_text)
	return sentAnalysis.get_polarity_score()

@app.get('/sentiment-subjectivity/{sentiment_text}')
async def subjectivity_score(sentiment_text):
	sentAnalysis = SentimentAnalysis(sentiment_text)
	return sentAnalysis.get_subjectivity_score()

#/ip-address/10.0.0.1?server_ip=10.0.0.1
@app.get('/ip-address/{ip_address}')
async def ip_address(ip_address):#, server_ip: str = "127.0.0.1"):
	ipAddress = IPAddress(ip_address)#, server_ip)
	return ipAddress.get_ip_details() 

@app.post("/face-count/")
async def face_count(file: bytes = File(...)):	
	facesCount = FacialCount()
	return facesCount.get_face_count(file)

@app.post("/face-recognition-set/")
async def face_recognition_set(file: bytes = File(...)):	
	faceRecognition = FacialRecognition()
	return faceRecognition.set_face_to_find(file)
	
@app.post("/face-recognition/")
async def face_recognition(file: bytes = File(...)):	
	faceRecognition = FacialRecognition()
	return faceRecognition.compare_face(file)
