# Camera.py
# written by Harrison Noble

import io
import numpy as np
import cv2 
#from picamera import PiCamera

class Camera:

	def __init__(self):
		
		#create face and profile classifiers
		self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
		self.profile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml")

		self.num_people = 0

		self.stream = io.BytesIO()
		#self.camera = PiCamera()


	def detect_people(self):
		'''Function to determine number of people in the room'''

		pass
		
	def get_num_people(self):
		'''Function that returns number of people in the room'''
		self.detect_people()
		return self.num_people




