# SettingsCameras.py
# written by Harrison Noble

import tkinter as tk

class SettingsCameras(tk.Frame):
	'''Description'''
	
# --------------------- Init Function  ---------------------

	def __init__(self, parent, thermostat):
		#initialize frame and handle format
		tk.Frame.__init__(self, parent)
		self.config(bg='#525252')
		self.grid(row=1, column=0, rowspan=6, columnspan = 2, sticky='nesw')
		self.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
		self.columnconfigure((0, 1), weight=1)

		self._therm = thermostat

		#TODO

# --------------------- End Init Function  ---------------------

# --------------------- Helper Functions  ---------------------

#TODO

# --------------------- End Helper Functions  ---------------------