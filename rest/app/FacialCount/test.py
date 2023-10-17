import requests
import json

# import cv2
# import numpy as np


# curl -F ‘data=@path/to/local/file’ UPLOAD_ADDRESS

# url = 'http://127.0.0.1:80/face-count/'
# # files = {'media': open('test.jpg', 'rb')}
# # response = requests.post(url, files=files)
# # print(response)

# # # url = "http://localhost:5000/"
# fin = open('test.jpg', 'rb')
# files = {'file': fin}
# try:
# 	r = requests.post(url, files=files)
# 	print (r.text)
# finally:
# 	fin.close()


# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# # Read the input image
# img = cv2.imread('test.jpeg')
# # Convert into grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # Detect faces
# faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# print(len(faces))
# # Draw rectangle around the faces
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# # Display the output
# cv2.imshow('img', img)
# cv2.waitKey()

url = 'http://127.0.0.1:80/face-recognition-set/'
fin = open('/Users/james/Documents/test-data/faces/Stephen_Stewart.png', 'rb')
files = {'file': fin}
try:
	r = requests.post(url, files=files)
	print(r.text)
finally:
	fin.close()


# url = 'http://127.0.0.1:80/face-recognition-set/'
# files = {'media': open('/Users/james/Documents/test-data/faces/Stephen_Stewart.png', 'rb')}
# r = requests.post(url, files=files)
# print(r)
url = 'http://127.0.0.1:80/face-recognition/'
fin = open('/Users/james/Documents/test-data/faces/maxresdefault.jpg', 'rb')
files = {'file': fin}
try:
	r = requests.post(url, files=files)
	print (r.text)
finally:
	fin.close()
