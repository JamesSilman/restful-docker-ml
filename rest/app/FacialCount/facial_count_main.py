import os
import cv2
import json
import numpy as np

class FacialCount:

	def get_face_count(self, file):

		face_cascade = cv2.CascadeClassifier('FacialCount/haarcascade_frontalface_default.xml')
		nparr = np.fromstring(file, np.uint8)
		img = cv2.imdecode(nparr, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(img, 1.3, 4)
		return {"face_count": json.dumps(len(faces))}


