# SettingsRight.py
# written by Harrison Noble

import tkinter as tk

class SettingsRight(tk.Frame):
	'''SettingsRight handles displaying the right side of the settings page. Arguements 
	are: 'parent' which is the frame object that creates this class, and 'thermostat' 
	which is the thermostat object created at the beginning of execution.'''
	
# --------------------- Init Function  ---------------------

	def __init__(self, parent, thermostat):
		#initialize frame and handle format
		tk.Frame.__init__(self, parent)
		self.config(bg='#525252')
		self.grid(row=1, column=2, rowspan=3, columnspan = 2, 
				  sticky='nesw', pady=(0, 20), padx=(5, 15))
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)

		self._therm = thermostat

		#TODO

# --------------------- End Init Function  ---------------------

# --------------------- Helper Functions  ---------------------

#TODO

# --------------------- End Helper Functions  ---------------------