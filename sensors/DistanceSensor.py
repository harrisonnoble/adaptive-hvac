# DistanceSensor.py
# written by Harrison Noble

import RPi.GPIO as GPIO
import time

class DistanceSensor:
	'''DistanceSensor class to handle the interfacing to the HC-SR04 ultrasonic sensor'''

# --------------------- Init Function  ---------------------  

	def __init__(self):
		self._pin_trigger = 4
		self._pin_echo = 17

		GPIO.setup(self._pin_trigger, GPIO.OUT)
		GPIO.setup(self._pin_echo, GPIO.IN)

		GPIO.output(self._pin_trigger, GPIO.LOW)

		self._distance = 0

		self._update_distance()


# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  ---------------------  

	def _update_distance(self):
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
		self._update_distance()
		return self._distance

# --------------------- End Helper Functions  ---------------------  