# TempSensor.py
# written by Harrison Noble

#import utils.bme280 as bme

class TempSensor:
	'''Temerature sensor class to interface with BME 280 temperature sensor'''

# --------------------- Init Function  ---------------------  

	def __init__(self):
		self._temperature = 0.
		self._mode = 'F'

		self.update_temp()

# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  --------------------- 

	#getter function
	@property
	def mode(self):
		'''Returns whether temperature readings are in fahrenheit or celcius'''
		return self._mode 

	#helper functions
	def update_temp(self):
		'''Function to update the temperature variable.
		Uses bme280.py, a script made for the temperature sensor model'''
		#temp, _, _ = bme.readBME280All()
		#self._temperature = temp
		pass

	def get_temp(self):
		'''Function to update the temperature via the sensor and return the value.'''
		self.update_temp()
		# Depending on temperature mode (celcius or fahrenheit) return correct value
		if self._mode == 'C':
			return self._temperature
		return self.convert_to_f()

	def convert_to_f(self):
		'''Function to return temperature value in fahrenheit'''
		return ((self._temperature * 1.8) + 32)

	def toggle_mode(self):
		'''Toggle between fahrenheit or celcius modes'''
		self._mode = 'C' if self._mode == 'F' else 'F'
		return self._mode

# --------------------- End Helper Functions  ---------------------  