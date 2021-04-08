# ThermCamera.py
# written by Harrison Noble

from busio import I2C
from adafruit_amg88xx import AMG88XX
from colour import Color
import numpy as np
import cv2
import board

class ThermalCamera:
	'''ThermalCamera class to handle the interfacing to the AMG8833 IR thermal camera'''

# --------------------- Init Function  ---------------------  

	def __init__(self):
		self._MIN_TEMP = 0
		self._MAX_TEMP = 0
		self._COLOR_DEPTH = 1024
		self._blue = Color('indigo')
		self._colors = list(self._blue.range_to(Color('red'), self._COLOR_DEPTH))
		self._colors = [(int(c.red * 255), int(c.green * 255), int(c.blue * 255)) for c in self._colors]

		self._i2c = I2C(board.SCL, board.SDA)
		#self._amg = AMG88XX(self._i2c)

# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  ---------------------  

	def _map_val(self, p):
		return (p - self._MIN_TEMP) * (self._COLOR_DEPTH) / (self._MAX_TEMP - self._MIN_TEMP)

	def _process_img(self):
		pixels = []
		for row in self._amg.pixels:
			pixels = pixels + row
		pixels = [self._map_val(p) for p in pixels]

		#INTERPOLATION

	#getter
	@property
	def therm_img(self):
		'''Property to get the thermal image from camera'''
		return #self._amg.pixels

# --------------------- End Helper Functions  ---------------------  