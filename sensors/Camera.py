# Camera.py
# written by Harrison Noble

import io
import numpy as np
import cv2 
from picamera import PiCamera

class Camera:
	'''Camera class interfaces with raspberry pi camera module. Contains the 
	machine learning model to determine number of people in the room.'''

# --------------------- Init Function  ---------------------  

	def __init__(self):
		
		#create face and profile classifiers
		self._face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
		self._profile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml")

		self._num_people = 0

		self._stream = io.BytesIO()
		self.camera = PiCamera()

# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  ---------------------  

	def detect_people(self):
		'''Function to determine number of people in the room'''

		pass
	
	@property
	def num_people(self):
		'''Function that returns number of people in the room'''
		self.detect_people()
		return self._num_people

# --------------------- End Helper Functions  ---------------------  