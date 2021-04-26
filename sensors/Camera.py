# Camera.py
# written by Harrison Noble

import io
import numpy as np
import cv2 
from picamera import PiCamera

class Camera:
	'''Camera class interfaces with raspberry pi camera module. Contains the 
	machine learning model to determine number of people in the room'''

# --------------------- Init Function  ---------------------  

	def __init__(self):
		#create face and profile classifiers
		self._face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
		self._profile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml")

		self._num_people = 0

		#create memory stream so photos dont have to be saved as files
		self._stream = io.BytesIO()

		self._streaming_img = False
		self._detecting_faces = False

# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  ---------------------  

	def _detect_people(self, write_img=False):
		'''Function to detect number of people in the room'''
		#dont detect faces if camera is streaming
		if self._streaming_img:
			print('Camera busy... skipping detection')
			return

		#adjust camera settings and send the image to memory stream
		self._detecting_faces = True
		try:
			with PiCamera() as camera:
				camera.rotation = 90
				camera.resolution = (224, 144)
				camera.capture(self._stream, format='jpeg')
		except:
			print('Camera error... skipping detection')
			return

		#convert image to numpy array and use that to create an OpenCV image
		image = np.frombuffer(self._stream.getvalue(), dtype=np.uint8)
		self._stream.seek(0)
		self._stream.truncate(0)
		self._detecting_faces = False
		image = cv2.imdecode(image, 1)

		#convert to grayscale and look for faces in image using the cascade classifier
		image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		faces = self._face_cascade.detectMultiScale(image, 1.1, 5)
		profiles = self._profile_cascade.detectMultiScale(image, 1.1, 5)

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

		print('Found', str(len(faces)), 'faces and', str(len(profiles)), 'profiles')

		#save number of people to the num_people variable
		self._num_people = len(faces) + len(profiles)

		#save image to a 'result.jpg' if parameter is true
		if write_img:
			for (x, y, w, h) in faces:
				cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)
			for (x, y, w, h) in profiles:
				cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 255), 2)
			cv2.imwrite('result.jpg', image)

	#getters
	@property
	def img(self):
		'''property that returns memory stream of the camera image'''
		#dont stream if camera is detecting faces
		if self._detecting_faces:
			print('Camera detecting faces... skipping stream')
			return

		#adjust camera settings and send the image to memory stream
		self._streaming_img = True
		try:
			with PiCamera() as camera:
				camera.rotation = 90
				camera.resolution = (224, 144)
				camera.capture(self._stream, format='jpeg')
		except:
			print('Camera error... skipping stream')
			return

		#convert image to numpy array and use that to create an RGB OpenCV image
		image = np.frombuffer(self._stream.getvalue(), dtype=np.uint8)
		self._stream.seek(0)
		self._stream.truncate(0)
		self._streaming_img = False
		image = cv2.imdecode(image, 1)
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		return image
	
	@property
	def num_people(self):
		'''property that runs the facial detection and returns number of people'''
		self._detect_people()
		return self._num_people

# --------------------- End Helper Functions  ---------------------  