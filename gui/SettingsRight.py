# SettingsRight.py
# written by Harrison Noble

import tkinter as tk

class SettingsRight(tk.Frame):
	'''Description'''
	
# --------------------- Init Function  ---------------------

	def __init__(self, parent, thermostat):
		#initialize frame and handle format
		tk.Frame.__init__(self, parent)
		self.config(bg='#525252')
		self.grid(row=1, column=2, rowspan=3, columnspan = 2, 
				  sticky='nesw', pady=(0, 20), padx=(5, 15))
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)

		#TODO

# --------------------- End Init Function  ---------------------

# --------------------- Helper Functions  ---------------------

#TODO

# --------------------- End Helper Functions  ---------------------