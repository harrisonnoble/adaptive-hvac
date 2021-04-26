# ThermCamera.py
# written by Harrison Noble

from busio import I2C
from adafruit_amg88xx import AMG88XX
from colour import Color
import numpy as np
import cv2
import board
import imutils

class ThermalCamera:
	'''ThermalCamera class to handle the interfacing to the AMG8833 IR thermal camera'''

# --------------------- Init Function  ---------------------  

	def __init__(self):
		self._MIN_TEMP = 20.
		self._MAX_TEMP = 32.
		self._COLOR_DEPTH = 1024
		self._blue = Color('indigo')
		self._colors = list(self._blue.range_to(Color('red'), self._COLOR_DEPTH))
		self._colors = [[int(c.red * 255), int(c.green * 255), int(c.blue * 255)] for c in self._colors]

		self._i2c = I2C(board.SCL, board.SDA)
		self._amg = AMG88XX(self._i2c)

# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  ---------------------  

	def _map_val(self, p):
		'''map thermal camera readings to pixel values'''
		return (p - self._MIN_TEMP) * (self._COLOR_DEPTH - 1) / (self._MAX_TEMP - self._MIN_TEMP)

	def _constrain(self, p):
		return min((self._COLOR_DEPTH - 1), max(0, int(p)))

	def _process_img(self):
		'''function to process the thermal image into an actual image'''
		pixels = []
		for row in self._amg.pixels:
			row = [self._map_val(p) for p in row]
			row = [self._colors[self._constrain(p)] for p in row]
			pixels.append(row)
		
		pixels = np.asarray(pixels, dtype='uint8')
		pixels = cv2.resize(pixels, None, fx=17, fy=17, interpolation=cv2.INTER_CUBIC)
		pixels = imutils.rotate(pixels, 90)

		return pixels

	#getter
	@property
	def therm_img(self):
		'''Property to get the thermal image from camera'''
		try:
			return self._process_img()
		except:
			print('Error getting thermal image')
			return

# --------------------- End Helper Functions  ---------------------  