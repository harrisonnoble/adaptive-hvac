# camera.py
# written by Harrison Noble

import io
import numpy as np
import cv2 
#from picamera import PiCamera

class Camera:

	def __init__(self):
		super().__init__()

		self.stream = io.BytesIO()
		#self.camera = PiCamera()


	def detect_people(self):
		#create face and profile classifiers
		face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
		profile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml")
		
		
		pass
		




