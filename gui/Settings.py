# Settings.py
# written by Harrison Noble

import tkinter as tk
from tkinter.constants import S
from gui.SettingsLeft import SettingsLeft
from gui.SettingsRight import SettingsRight
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

		#create back button and display
		self.back_img = tk.PhotoImage(file=curr_path + '/imgs/back.png').subsample(4, 4)
		self.toggle_btn = tk.Label(self, image=self.back_img, borderwidth=0)
		self.toggle_btn.bind('<Button-1>', lambda e: controller.show_dashboard())
		self.toggle_btn.grid(column=0, row=0, sticky='nw', padx=10, pady=5)

		#create time label and display
		self.time_label = tk.Label(self, font=('calibri', 35),
								   bg='#121212', fg='white')
		self.time_label.grid(column=1, row=0, sticky='new', columnspan=2, pady=5)

		#create current temperature label and display
		self.curr_temp = self._thermostat.curr_temp
		self.curr_temp_lbl = tk.Label(self, font=('calibri', 35), bg='#121212', 
									  fg='white', text=str(self.curr_temp) + '°')
		self.curr_temp_lbl.grid(column=3, row=0, sticky='ne', padx=10, pady=5)

		#create left and right side of settings page
		self.left = SettingsLeft(self, thermostat)
		self.right = SettingsRight(self, thermostat)
		
		#call the update functions
		self.update_time()
		self.update_curr_temp()

# --------------------- End Init Function  ---------------------

# --------------------- Helper Functions  ---------------------

	def update_time(self):
		'''Function to update the displayed time every 30 seconds'''
		self.time_label.config(text=strftime('%-I:%M %p'))
		self.time_label.after(30000, self.update_time)

	def update_curr_temp(self):
		'''Function to update current temperature label'''
		self.curr_temp = self._thermostat.curr_temp
		self.curr_temp_lbl.config(text=str(self.curr_temp) + '°')
		self.curr_temp_lbl.after(10000, self.update_curr_temp)

# --------------------- End Helper Functions  ---------------------