# DistanceSensor.py
# written by Harrison Noble

class DistanceSensor:
	'''DistanceSensor class to handle the interfacing to the HC-SR04 ultrasonic sensor'''

# --------------------- Init Function  ---------------------  

	def __init__(self):

		self._distance = 0

# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  ---------------------  

	@property
	def distance(self):
		'''property to get the distance reading'''
		return self._distance

# --------------------- End Helper Functions  ---------------------  