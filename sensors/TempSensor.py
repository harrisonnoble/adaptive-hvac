# TempSensor.py
# written by Harrison Noble

import utils.bme280 as bme

class TempSensor:

	def __init__(self):
		self.temperature = 0
		self.mode = 'C'

		self.update_temp()

	def update_temp(self):
		'''Function to update the temperature variable.
		Uses bme280.py, a script made for the temperature sensor model'''

		temp, pressure, humidity = bme.readBME280All()
		self.temperature = temp

	def get_temp(self):
		'''Function to update the temperature via the sensor and return the value.'''

		self.update_temp()
		# Depending on temperature mode (celcius or fahrenheit) return correct value
		if self.mode is 'C':
			return self.temperature
		return self.convert_to_f()

	def convert_to_f(self):
		'''Function to return temperature value in fahrenheit'''
		return ((self.temperature * 1.8) + 32)

	def toggle_mode(self):
		'''Toggle between fahrenheit or celcius modes'''
		self.mode = 'C' if self.mode is 'F' else 'C'