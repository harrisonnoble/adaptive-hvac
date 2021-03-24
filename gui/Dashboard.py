# Dashboard.py
# written by Harrison Noble

import tkinter as tk
from time import strftime
import os

class Dashboard(tk.Frame): 
	'''Dashboard class that manages displaying current temperature, desired
	temperature, fan control, and heat/cool control. Functionality to update
	desired temperature, heat/cool mode and fan control handled in this class. 
	Arguements are: 'parent' which is the frame object that creates this class, 
	'controller' which handles the swapping between the settings page and dashboard, 
	and 'thermostat' which is the thermostat object created at the beginning of execution.'''

# --------------------- Init Function ---------------------   

	def __init__(self, parent, controller, thermostat):
		#initialization for frame object (dashboard UI)
		tk.Frame.__init__(self, parent)
		self.config(bg='#121212')

		#get current path
		curr_path = os.path.dirname(os.path.realpath(__file__))

		#initialize thermostat in order to run functions
		self._therm = thermostat

		#layout management
		for i in range(0, 4):
			self.rowconfigure(i, weight=1)
			self.columnconfigure(i, weight=1, min='200')

		#create top row (time and settings toggle) and display items
		#--------------------------------------------
		self.time_lbl = tk.Label(self, font=('calibri', 32),
								 bg='#121212', fg='white')

		self.settings = tk.PhotoImage(file=curr_path + '/imgs/settings.png').subsample(4,4)
		self.toggle_btn = tk.Label(self, image=self.settings, borderwidth=0)
		self.toggle_btn.bind('<Button-1>', lambda e: controller.show_settings())

		self.time_lbl.grid(column=1, row=0, sticky='new', columnspan=2, pady=5)
		self.toggle_btn.grid(column=3, row=0, sticky='ne', padx=10, pady=5)
		#--------------------------------------------

		#create left side of dashboard and display items
		#--------------------------------------------
		#configure left side of page as a frame
		self.left = tk.Frame(self)
		self.left.config(bg='#121212')
		self.left.grid(row=1, column=0, rowspan=3, sticky='nesw')
		self.left.rowconfigure((0, 1, 2, 3, 4), weight=1, min='30')
		self.left.columnconfigure(0, weight=1, min='200')

		#create labels for variables, variable descriptions, and backgrounds
		self.mode_bg = tk.Label(self.left, bg='#525252', width=12)
		self.mode_bg.bind('<Button-1>', lambda e: self.change_mode())
		self.mode_lbl = tk.Label(self.left, text='Mode', font=('calibri', 11),
								 bg='#525252', fg='white')
		self.mode_stng = tk.Label(self.left, font=('calibri', 13),
								  bg='#525252', text=self._therm.mode,
								  fg='#ff1212' if self._therm.mode == 'Heat' else '#0062ff')
		self.mode_stng.bind('<Button-1>', lambda e: self.change_mode())
		
		self.fan_bg = tk.Label(self.left, bg='#525252', width=12)
		self.fan_bg.bind('<Button-1>', lambda e: self.toggle_fan())
		self.fan_lbl = tk.Label(self.left, text='Fan', font=('calibri', 11),
								bg='#525252', fg='white')
		self.fan_stng = tk.Label(self.left, font=('calibri', 13),
								 bg='#525252', fg='white',
								 text='On' if self._therm.fan else 'Off')
		self.fan_stng.bind('<Button-1>', lambda e: self.toggle_fan())

		self.system_bg = tk.Label(self.left, bg='#525252', width=12)
		self.system_lbl = tk.Label(self.left, text='System', font=('calibri', 11),
								   bg='#525252', fg='white')
		self.system_stng = tk.Label(self.left, font=('calibri', 13),
									bg='#525252', fg='white',
									text=self._therm.system)						

		#display components of left side of screen
		self.mode_bg.grid(row=0, column=0, sticky='ns', pady=(0, 15))
		self.mode_lbl.grid(row=0, column=0, sticky='n')
		self.mode_stng.grid(row=0, column=0)
		self.fan_bg.grid(row=1, column=0, sticky='ns', pady=(0, 15))
		self.fan_lbl.grid(row=1, column=0, sticky='n')
		self.fan_stng.grid(row=1, column=0)
		self.system_bg.grid(row=2, column=0, sticky='ns', pady=(0, 15))
		self.system_lbl.grid(row=2, column=0, sticky='n')
		self.system_stng.grid(row=2, column=0)
		#--------------------------------------------

		#create middle of dashboard
		#--------------------------------------------
		#configuring middle frame
		self.middle = tk.Frame(self)
		self.middle.config(bg='#121212')
		self.middle.grid(row=1, column=1, columnspan=2, rowspan=3, sticky='nesw')
		self.middle.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
		self.middle.columnconfigure((0, 1, 2), weight=1)

		#create variables for temperature labels and temperature measurements
		self.bg = tk.PhotoImage(file=curr_path + '/imgs/bg.png')
		self.bg = self.bg.subsample(1, 1)
		self.bg_img = tk.Label(self.middle, image=self.bg, borderwidth=0)

		self.curr_temp_lbl2 = tk.Label(self.middle, font=('calibri', 14),
									   bg='#525252', fg='white',
									   text='Current Temp')
		self.curr_temp_lbl = tk.Label(self.middle, font=('calibri', 38),
									  bg='#525252', fg='white',
									  text=str(self._therm.curr_temp) + '°')
		self.desired_temp_lbl = tk.Label(self.middle, font=('calibri', 30), 
										 bg='#121212', fg='white', 
										 text=str(self._therm.desired_temp) + '°')
		self.desired_temp_lbl2 = tk.Label(self.middle, font=('calibri', 14), 
										  bg='#121212', fg='white', 
										  text='Desired Temp')

		#temperature increment / decrement buttons
		self.temp_down = tk.Label(self.middle, font=('calibri', 34),
								  bg='#121212', fg='white', text='-')
		self.temp_down.bind('<Button-1>', lambda e: self.dec_temp())

		self.temp_up = tk.Label(self.middle, font=('calibri', 34),
								bg='#121212', fg='white', text='+')
		self.temp_up.bind('<Button-1>', lambda e: self.inc_temp())								

		#display middle components
		self.curr_temp_lbl.grid(column=0, row=1, columnspan=3)
		self.curr_temp_lbl2.grid(column=0, row=2, columnspan=3, sticky='n')
		self.bg_img.grid(column=0, row=0, columnspan=3, rowspan=3)

		self.temp_down.grid(column=0, row=3, sticky='se')
		self.desired_temp_lbl.grid(column=1, row=3, sticky='s')
		self.temp_up.grid(column=2, row=3, sticky='sw')

		self.desired_temp_lbl2.grid(column=1, row=4, sticky='n')
		#--------------------------------------------

		self.time_stopper = None
		self.curr_temp_stopper = None
		self.fan_stopper = None

		#call starter function to update values
		self.starter()

# --------------------- End Init Function ---------------------

# --------------------- Helper Functions  ---------------------

	def update_time(self):
		'''Function to update the displayed time every 30 seconds'''
		t = strftime('%-I:%M %p')
		self.time_lbl.config(text=t)
		self.time_lbl.after(30000, self.update_time)

	def update_curr_temp(self):
		'''Function to update current temperature label'''
		self.curr_temp_lbl.config(text=str(self._therm.curr_temp) + '°')
		self.curr_temp_lbl.after(200, self.update_curr_temp)

	def inc_temp(self):
		'''Function to increment desired temperature label'''
		if self._therm.is_on:
			self._therm.inc_desired_temp()
			#update label
			self.desired_temp_lbl.config(text=str(self._therm.desired_temp) + '°')
	
	def dec_temp(self):
		'''Function to decrement desired temperature label'''
		if self._therm.is_on:
			self._therm.dec_desired_temp()
			#update label
			self.desired_temp_lbl.config(text=str(self._therm.desired_temp) + '°')

	def change_mode(self):
		'''Function to change the mode (heat/cool) of the thermostat'''
		#check if thermostat is on and change mode/label if it is
		if self._therm.is_on:
			self._therm.switch_mode()
			self.mode_stng.config(text=self._therm.mode,
								  fg='#ff1212' if self._therm.mode == 'Heat' else '#0062ff')
		else:
			#if thermostat is off display off
			self.mode_stng.config(text='Off', fg='white')

	def toggle_fan(self):
		'''Toggles the fan on and off if thermostat is in manual setting'''
		if self._therm.system == 'Manual':
			self._therm.toggle_fan()
			self.fan_stng.config(text='On' if self._therm.fan else 'Off')

	def update_fan(self):
		'''Check if fan setting has changed after time period and update if so'''
		self.fan_stng.config(text='On' if self._therm.fan else 'Off')
		self.fan_stopper = self.fan_stng.after(500, self.update_fan)

	def check_labels(self):
		'''Checks the label values of data that could have been changed in settings
		and update accordingly'''
		if self._therm.is_on:
			#update left side labels
			self.mode_stng.config(text=self._therm.mode,
								  fg='#ff1212' if self._therm.mode == 'Heat' else '#0062ff')
			self.fan_stng.config(text='On' if self._therm.fan else 'Off')
			self.system_stng.config(text=self._therm.system)
			#update desired temp (between C or F if changed)
			self.desired_temp_lbl.config(text=str(self._therm.desired_temp) + '°')
		else:
			#update left side labels
			self.mode_stng.config(text='Off', fg='white')
			self.fan_stng.config(text='Off')
			self.system_stng.config(text='Off')
			#update desired temperature 
			self.desired_temp_lbl.config(text='Off')

	def stopper(self):
		if self.time_stopper:
			self.time_lbl.after_cancel(self.time_stopper)
			self.time_stopper = None
		if self.curr_temp_stopper:
			self.curr_temp_lbl.after_cancel(self.curr_temp_stopper)
			self.curr_temp_stopper = None
		if self.fan_stopper:
			self.fan_stng.after_cancel(self.fan_stopper)
			self.fan_stopper = None

	def starter(self):
		self.update_time()
		self.update_curr_temp()
		self.update_fan()
		self.check_labels()

# --------------------- End Helper Functions  ---------------------