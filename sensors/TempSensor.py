# TempSensor.py
# written by Harrison Noble

from utils import bme280

class TempSensor:
	'''Temerature sensor class to interface with BME 280 temperature sensor'''

# --------------------- Init Function  ---------------------  

	def __init__(self, mode=None):
		#make sure mode is either F or C, defaults to F
		if mode == 'F' or mode == 'C':
			self._mode = mode
		else:
			self._mode = 'F'

		self._temperature = 0.
		self._update_temp()

# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  ---------------------  

	def _update_temp(self):
		'''Function to update the temperature variable. Uses bme280.py, a script made for the temperature sensor'''
		temp, _, _ = bme280.readBME280All()
		self._temperature = temp

	def _convert_to_f(self):
		'''Function to return temperature value in fahrenheit'''
		return round(((self._temperature * 1.8) + 32), 1)

	def toggle_mode(self):
		'''Toggle between fahrenheit or celcius modes'''
		self._mode = 'C' if self._mode == 'F' else 'F'
		return self._mode

	#getters
	@property
	def mode(self):
		'''Returns whether temperature readings are in fahrenheit or celcius'''
		return self._mode

	@property
	def temp(self):
		'''property to update temperature via the sensor and return the value'''
		self._update_temp()
		# Depending on temperature mode (celcius or fahrenheit) return correct value
		if self._mode == 'C':
			return round(self._temperature, 1)
		return self._convert_to_f()

# --------------------- End Helper Functions  ---------------------  