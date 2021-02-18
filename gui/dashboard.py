# dashboard.py
# written by Harrison Noble

import tkinter as tk
from time import strftime
import os

class Dashboard(tk.Frame): 
	'''Dashboard description'''

# --------------------- Init Function ---------------------   

	def __init__(self, parent, controller, thermostat):
		#initialization for frame object (dashboard UI)
		tk.Frame.__init__(self, parent)   
		self.config(bg='#121212')

		#initialize thermostat in order to run functions
		self._thermostat = thermostat

		#layout management
		for i in range(0, 4):
			self.rowconfigure(i, weight=3)
			self.columnconfigure(i, weight=3, min='200')

		#get settings image
		curr_path = os.path.dirname(os.path.realpath(__file__))
		self.image = tk.PhotoImage(file=curr_path + '/imgs/settings.png')
		self.image = self.image.subsample(4, 4)

		#create a label with the settings image and bind show_settings function
		self.toggle_btn = tk.Label(self, image=self.image, borderwidth=0)
		self.toggle_btn.bind('<Button-1>', lambda e: controller.show_settings())

		#create label for the time
		self.time_lbl = tk.Label(self, font=('calibri', 35), bg='#121212', fg='white')

		#create temperature increment / decrement buttons
		self.temp_down = tk.Label(self, font=('calibri', 35), bg='#121212', fg='white', text='-')
		self.temp_down.bind('<Button-1>', lambda e: self.dec_temp())
		self.temp_up = tk.Label(self, font=('calibri', 35), bg='#121212', fg='white', text='+')
		self.temp_up.bind('<Button-1>', lambda e: self.inc_temp())

		#create variables for temperature
		self.curr_temp = self._thermostat.curr_temp
		self.curr_temp_lbl = tk.Label(self, font=('calibri', 40), bg='#525252', fg='white')
		self.desired_temp = self._thermostat.desired_temp
		self.desired_temp_lbl = tk.Label(self, font=('calibri', 30), 
										bg='#121212', fg='white', 
										text=str(self.desired_temp) + '°')

		#display all components
		self.time_lbl.grid(column=1, row=0, sticky='new', columnspan=2, pady=5)

		self.toggle_btn.grid(column=3, row=0, sticky='ne', padx=10, pady=5)

		self.curr_temp_lbl.grid(column=1, row=1, columnspan=2)
		self.desired_temp_lbl.grid(column=1, row=2, columnspan=2)

		self.temp_down.grid(column=1, row=2)
		self.temp_up.grid(column=2, row=2)

		#call functions to update values
		self.update_time()
		self.update_curr_temp() 

# --------------------- End Init Function ---------------------

# --------------------- Helper Functions  ---------------------

	def update_time(self):
		'''Function to update the displayed time every 30 seconds'''
		t = strftime('%-I:%M %p')
		self.time_lbl.config(text=t)
		self.time_lbl.after(30000, self.update_time)

	def update_curr_temp(self):
		'''Function to update current temperature label'''
		self.curr_temp = self._thermostat.curr_temp
		self.curr_temp_lbl.config(text=str(self.curr_temp) + '°')
		self.curr_temp_lbl.after(10000, self.update_curr_temp)

	def inc_temp(self, temp=None):
		'''Function to update desired temperature label'''
		self.desired_temp = self._thermostat.inc_desired_temp()
		self.desired_temp_lbl.config(text=str(self.desired_temp) + '°')
	
	def dec_temp(self):
		self.desired_temp = self._thermostat.dec_desired_temp()
		self.desired_temp_lbl.config(text=str(self.desired_temp) + '°')

# --------------------- End Helper Functions  ---------------------