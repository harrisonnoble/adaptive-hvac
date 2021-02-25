# Camera.py
# written by Harrison Noble

import io
import numpy as np
import cv2 
from picamera import PiCamera
import time

class Camera:
	'''Camera class interfaces with raspberry pi camera module. Contains the 
	machine learning model to determine number of people in the room.'''

# --------------------- Init Function  ---------------------  

	def __init__(self):
		
		#create face and profile classifiers
		self._face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
		self._profile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml")

		self._num_people = 0

		#create memory stream so photos dont have to be saved as files
		self._stream = io.BytesIO()

		#create camera
		self._camera = PiCamera()

# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  ---------------------  

	def detect_people(self, write_img=False):
		'''Function to determine number of people in the room'''

		#adjust camera settings and send the image to memory stream
		self._camera.resolution = (640, 360)
		self._camera.capture(self._stream, format='jpeg')

		#convert image to numpy array and use that to create an OpenCV image
		buffer = np.frombuffer(self._stream.getvalue(), dtype=np.uint8)
		image = cv2.imdecode(buffer, 1)

		#convert to grayscale and look for faces in image using the cascade classifier
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		faces = self._face_cascade.detectMultiScale(gray, 1.1, 5)
		profiles = self._profile_cascade.detectMultiScale(gray, 1.1, 5)

		#loop through all faces and profiles of faces detected
		profiles_not_faces = []
		for face in faces:
			f_bottom_left = (face[0], face[1] + face[3])
			f_top_right = (face[0] + face[2], face[1])

			for profile in profiles:
				p_bottom_left = (profile[0], profile[1] + profile[3])
				p_top_right = (profile[0] + profile[2], profile[1])
				
				#do not count profiles that overlap with a detected face. 
				#Logic checks if rectangles overlap, if they dont keep the classified profile
				if not (f_top_right[0] < p_bottom_left[0] or f_bottom_left[0] > p_top_right[0]
						or f_top_right[1] < p_bottom_left[1] or f_bottom_left[1] > p_top_right[1]):	
					profiles_not_faces.append(profile)

		profiles = profiles_not_faces

		print('Found', str(len(faces)), 'faces')
		print('Found', str(len(profiles)), 'profiles')

		#save number of people to the num_people variable
		self._num_people = len(faces)

		#save image to a 'result.jpg' if parameter is true
		if write_img:
			for (x, y, w, h) in faces:
				cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)
			for (x, y, w, h) in profiles:
				cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 255), 2)

			cv2.imwrite('result.jpg', image)

		self._stream.seek(0)
		self._stream.truncate(0)

	def get_img(self):
		#adjust camera settings and send the image to memory stream
		self._camera.resolution = (224, 144)
		self._camera.capture(self._stream, format='jpeg')

		#convert image to numpy array and use that to create an OpenCV image
		buffer = np.frombuffer(self._stream.getvalue(), dtype=np.uint8)
		image = cv2.imdecode(buffer, 1)

		self._stream.seek(0)
		self._stream.truncate(0)

		return image
		
	@property
	def num_people(self):
		'''Function that returns number of people in the room'''
		self.detect_people()
		return self._num_people

# --------------------- End Helper Functions  ---------------------  

# if __name__ == '__main__':
# 	cam = Camera()
# 	while True:
# 		cam.detect_people(write_img=True)
# 		time.sleep(2)