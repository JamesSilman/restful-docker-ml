import cv2
import json
import numpy as np
import face_recognition

class FacialRecognition:

	def set_face_to_find(self, file):

		nparr = np.fromstring(file, np.uint8)
		img = cv2.imdecode(nparr, cv2.COLOR_BGR2GRAY)
		cv2.imwrite('FacialRecognition/Known/known.jpg', img)

	def compare_face(self, file):

		nparr = np.fromstring(file, np.uint8)
		img = cv2.imdecode(nparr, cv2.COLOR_BGR2GRAY)
		cv2.imwrite('FacialRecognition/Unknown/unknown.jpg', img)

		known_image = face_recognition.load_image_file("FacialRecognition/Known/known.jpg")
		known_image_encoding = face_recognition.face_encodings(known_image)[0]
		
		unknown_picture = face_recognition.load_image_file("FacialRecognition/Unknown/unknown.jpg")
		unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

		results = face_recognition.compare_faces([known_image_encoding], unknown_face_encoding)

		if results[0] == True:
		    return {"facial-recognition": json.dumps("true")}
		
		return {"facial-recognition": json.dumps("false")}
