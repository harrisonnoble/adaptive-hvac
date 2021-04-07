# ThermCamera.py
# written by Harrison Noble

from busio import I2C
from adafruit_amg88xx import AMG88XX
import numpy as np
import cv2
import board

class ThermalCamera:
	'''ThermalCamera class to handle the interfacing to the AMG8833 IR thermal camera'''

# --------------------- Init Function  ---------------------  

	def __init__(self):
		self._i2c = I2C(board.SCL, board.SDA)
		#self._amg = AMG88XX(self._i2c)

# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  ---------------------  

	#getter
	@property
	def therm_img(self):
		'''Property to get the thermal image from camera'''
		return #self._amg.pixels

# --------------------- End Helper Functions  ---------------------  