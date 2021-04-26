# Settings.py
# written by Harrison Noble

import tkinter as tk
from gui import SettingsLeft, SettingsRight
from time import strftime
import os

class Settings(tk.Frame): 
	'''Settings class handles all administrative aspects of the thermostat including power,
	rebooting, sensor readings and max/min temperature operation ranges. Arguements are: 
	'parent' which is the frame object that creates this class, 'controller' which handles 
	the swapping between the settings page and dashboard, and 'thermostat' which is the 
	thermostat object created at the beginning of execution.'''

# --------------------- Init Function  ---------------------   

	def __init__(self, parent, controller, thermostat):
		#initialization for frame object (dashboard UI)
		tk.Frame.__init__(self, parent)   
		self.config(bg='#121212')
		self.rowconfigure(0, weight=1)
		self.rowconfigure(1, weight=15)
		self.columnconfigure((0, 1, 2, 3), weight=1, min='200')

		#initialize thermostat in order to run functions
		self._therm = thermostat

		#get current path to find images
		curr_path = os.path.dirname(os.path.realpath(__file__))

		#create back button and display
		self.back_img = tk.PhotoImage(file=curr_path + '/imgs/back.png').subsample(4, 4)
		self.toggle_btn = tk.Label(self, image=self.back_img, borderwidth=0)
		self.toggle_btn.bind('<Button-1>', lambda e: controller.show_dashboard())
		self.toggle_btn.grid(column=0, row=0, sticky='nw', padx=10, pady=5)

		#create time label and display
		self.time_label = tk.Label(self, font=('calibri', 32),
								   bg='#121212', fg='white')
		self.time_label.grid(column=1, row=0, sticky='new', columnspan=2, pady=5)

		#create current temperature label and display
		self.curr_temp_lbl = tk.Label(self, font=('calibri', 32), bg='#121212', 
									  fg='white', text=str(self._therm.curr_temp) + '°')
		self.curr_temp_lbl.grid(column=3, row=0, sticky='ne', padx=10, pady=5)

		#create left and right side of settings page
		self.left = SettingsLeft(self, thermostat)
		self.right = SettingsRight(self, thermostat)

		#variables to stop updates when not on page
		self._time_stopper = None
		self._temp_stopper = None

# --------------------- End Init Function  ---------------------

# --------------------- Helper Functions  ---------------------

	def _update_time(self):
		'''Function to update the displayed time every 10 seconds'''
		self.time_label.config(text=strftime('%-I:%M %p'))
		self._time_stopper = self.time_label.after(10000, self._update_time)

	def _update_curr_temp(self):
		'''Function to update current temperature label'''
		self.curr_temp_lbl.config(text=str(self._therm.curr_temp) + '°')
		self.left.update_temp_output()
		self._temp_stopper = self.curr_temp_lbl.after(3000, self._update_curr_temp)
	
	def update_curr_temp(self):
		'''Function to update current temp, called by SettingsRight when temp mode changed'''
		self.curr_temp_lbl.config(text=str(self._therm.curr_temp) + '°')
		self.left.update_temp_output()

	def stopper(self):
		'''Stop all updates'''
		if self._time_stopper:
			self.time_label.after_cancel(self._time_stopper)
			self._time_stopper = None
		if self._temp_stopper:
			self.curr_temp_lbl.after_cancel(self._temp_stopper)
			self._temp_stopper = None

		self.left.stopper()

	def starter(self):
		'''Begin updates'''
		self._update_time()
		self._update_curr_temp()
		self.left.starter()

# --------------------- End Helper Functions  ---------------------