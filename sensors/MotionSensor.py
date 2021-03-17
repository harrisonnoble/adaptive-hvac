# MotionSensor.py
# written by Harrison Noble

from gpiozero import MotionSensor as MS

class MotionSensor:
	'''MotionSensor class to interface with the HC-SR501 motion sensor.'''

# --------------------- Init Function  ---------------------  

	def __init__(self):
		self._motion = False

		self._sensor = MS(4)

		self._sensor.when_motion = self.on_motion
		self._sensor.when_no_motion = self.no_motion

		self._motion_func = None

# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  ---------------------  

	def set_motion_func(self, func):
		'''Function used to add an additional function call when motion is detected.'''

		if func:
			self._motion_func = func

	def on_motion(self):
		'''Function that is called when motion sensor detects motion'''

		if self._motion_func:
			self._motion_func()

		self._motion = True

	def no_motion(self):
		'''Function called when motion sensor stops detecting motion'''

		self._motion = False
		print('no motion')

	@property
	def motion(self):
		return self._motion

# --------------------- End Helper Functions  ---------------------  