# MotionSensor.py
# written by Harrison Noble

from gpiozero import MotionSensor as MotionSense
import time

class MotionSensor:
	'''MotionSensor class to interface with the HC-SR501 motion sensor'''

# --------------------- Init Function  ---------------------  

	def __init__(self):
		self._motion = False

		self._sensor = MotionSense(4)
		self._sensor.when_motion = self._on_motion
		self._sensor.when_no_motion = self._no_motion

		self._motion_func = None
		self._no_motion_func = None

# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  ---------------------  

	def _on_motion(self):
		'''Function that is called when motion sensor detects motion'''
		self._motion = True
		if self._motion_func:
			self._motion_func()
		time.sleep(5)

	def _no_motion(self):
		'''Function called when motion sensor stops detecting motion'''
		self._motion = False
		if self._no_motion_func:
			self._no_motion_func()

	def set_motion_func(self, func=None):
		'''Function used to add an additional function call when motion is detected.'''
		self._motion_func = func

	def set_no_motion_func(self, func=None):
		'''Function used to add an additional function call when no motion is detected.'''
		self._no_motion_func = func

	@property
	def motion(self):
		'''property that returns motion boolean'''
		return self._motion

# --------------------- End Helper Functions  ---------------------  