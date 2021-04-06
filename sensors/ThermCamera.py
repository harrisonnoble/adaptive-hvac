# ThermCamera.py
# written by Harrison Noble

class ThermalCamera:
	'''ThermalCamera class to handle the interfacing to the AMG8833 IR thermal camera'''

# --------------------- Init Function  ---------------------  

	def __init__(self):
		self._therm_img = None
		pass

# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  ---------------------  

	def update_img(self):
		'''Function to update thermal image variable'''
		pass

	#getter
	@property
	def therm_img(self):
		'''Property to get the thermal image from camera'''
		return self._therm_img

# --------------------- End Helper Functions  ---------------------  