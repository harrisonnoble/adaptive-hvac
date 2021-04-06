# DistanceSensor.py
# written by Harrison Noble

import RPi.GPIO as GPIO
import time

class DistanceSensor:
	'''DistanceSensor class to handle the interfacing to the HC-SR04 ultrasonic sensor'''

# --------------------- Init Function  ---------------------  

	def __init__(self):
		self._pin_trigger = 7
		self._pin_echo = 11

		#TODO: Set up GPIO to read sensor

		self._distance = 0

		#self.update_distance()


# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  ---------------------  

	def update_distance(self):
		'''function to update the distance reading'''
		#trigger sensor reading
		GPIO.output(self._pin_trigger, GPIO.HIGH)
		time.sleep(0.00001)
		GPIO.output(self._pin_trigger, GPIO.LOW)

		#wait for response and calculate time it took
		while GPIO.input(self._pin_echo) == 0:
			start_time = time.time()
		while GPIO.input(self._pin_echo) == 1:
			end_time = time.time()
		duration = end_time - start_time

		#update distance value (ultrasonic pulse travels 562.66 ft/s)
		self._distance = round(duration * 562.66)

	#getter
	@property
	def distance(self):
		'''property to get the distance reading'''
		return self._distance

# --------------------- End Helper Functions  ---------------------  