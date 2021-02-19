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

		#get current path to find images
		curr_path = os.path.dirname(os.path.realpath(__file__))

		#layout management
		self.rowconfigure(0, weight=1)
		self.rowconfigure((1, 2, 3), weight=5)
		self.columnconfigure((0, 1, 2, 3), weight=1, min='200')

		#create top row (time and settings toggle) and display items
		#--------------------------------------------
		#create a label with the back image and bind show_dashboard function
		self.back_img = tk.PhotoImage(file=curr_path + '/imgs/back.png').subsample(4, 4)
		self.toggle_btn = tk.Label(self, image=self.back_img, borderwidth=0)
		self.toggle_btn.bind('<Button-1>', lambda e: controller.show_dashboard())

		#create label for the time
		self.time_label = tk.Label(self, font=('calibri', 35),
									bg='#121212', fg='white')

		#create label to display current temperature
		self.curr_temp = self._thermostat.curr_temp
		self.curr_temp_lbl = tk.Label(self, font=('calibri', 35),
									bg='#121212', fg='white')

		#display all components in top row
		self.toggle_btn.grid(column=0, row=0, sticky='nw', padx=10, pady=5)
		self.time_label.grid(column=1, row=0, sticky='new', columnspan=2, pady=5)
		self.curr_temp_lbl.grid(column=3, row=0, sticky='ne', padx=10, pady=5)
		#--------------------------------------------

		#create left side of settings page
		#--------------------------------------------
		#frame configuration
		self.left = tk.Frame(self)
		self.left.config(bg='#525252')
		self.left.grid(row=1, column=0, rowspan=3, columnspan = 2, 
						sticky='nesw', pady=(0, 20), padx=(15, 5))
		self.left.rowconfigure(0, weight=1)
		self.left.columnconfigure(0, weight=1)

		#TODO: Create sensor/camera outputs
		#--------------------------------------------

		#create right side of settings page
		#--------------------------------------------
		#frame configuration
		self.right = tk.Frame(self)
		self.right.config(bg='#525252')
		self.right.grid(row=1, column=2, rowspan=3, columnspan = 2, 
						sticky='nesw', pady=(0, 20), padx=(5, 15))
		self.right.rowconfigure(0, weight=1)
		self.right.columnconfigure(0, weight=1)

		#TODO: Create different settings management
		#--------------------------------------------
		
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