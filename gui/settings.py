# settings.py
# written by Harrison Noble

import tkinter as tk
from time import strftime
import os

class Settings(tk.Frame): 
	'''Settings class handles all administrative aspects of the thermostat
	including power, rebooting, sensor readings and max/min temperature
	operation ranges.'''

# --------------------- Init Function  ---------------------   

	def __init__(self, parent, controller, thermostat):
		#initialization for frame object (dashboard UI)
		tk.Frame.__init__(self, parent)   
		self.config(bg='#121212')

		#initialize thermostat in order to run functions
		self._thermostat = thermostat

		#layout management
		for i in range(0, 4):
			self.rowconfigure(i, weight=1)
			self.columnconfigure(i, weight=1, min='200')

		#get back image
		curr_path = os.path.dirname(os.path.realpath(__file__))
		self.image = tk.PhotoImage(file=curr_path + '/imgs/back.png')
		self.image = self.image.subsample(4, 4)

		#create a label with the back image and bind show_dashboard function
		self.toggle_btn = tk.Label(self, image=self.image, borderwidth=0)
		self.toggle_btn.bind('<Button-1>', lambda e: controller.show_dashboard())

		#create label for the time
		self.time_label = tk.Label(self, font=('calibri', 35),
									bg='#121212', fg='white')

		#create label to display current temperature
		self.curr_temp = self._thermostat.curr_temp
		self.curr_temp_lbl = tk.Label(self, font=('calibri', 35),
									bg='#121212', fg='white')

		#display all components
		self.toggle_btn.grid(column=0, row=0, sticky='nw', padx=10, pady=5)
		self.time_label.grid(column=1, row=0, sticky='new', columnspan=2, pady=5)
		self.curr_temp_lbl.grid(column=3, row=0, sticky='ne', padx=10, pady=5)
		
		#call the update functions
		self.update_time()
		self.update_curr_temp()

# --------------------- End Init Function  ---------------------

# --------------------- Helper Functions  ---------------------

	def update_time(self):
		'''Function to update the displayed time every 30 seconds'''
		t = strftime('%-I:%M %p')
		self.time_label.config(text=t)
		self.time_label.after(30000, self.update_time)

	def update_curr_temp(self):
		'''Function to update current temperature label'''
		self.curr_temp = self._thermostat.curr_temp
		self.curr_temp_lbl.config(text=str(self.curr_temp) + '°')
		self.curr_temp_lbl.after(10000, self.update_curr_temp)

# --------------------- End Helper Functions  ---------------------