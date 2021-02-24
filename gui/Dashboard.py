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
		self._thermostat = thermostat

		#layout management
		for i in range(0, 4):
			self.rowconfigure(i, weight=1)
			self.columnconfigure(i, weight=1, min='200')

		#create top row (time and settings toggle) and display items
		#--------------------------------------------
		self.time_lbl = tk.Label(self, font=('calibri', 35),
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

		#define variables to display
		self.mode = self._thermostat.mode
		self.fan = self._thermostat.fan
		self.system = self._thermostat.system

		#create labels for variables, variable descriptions, and backgrounds
		self.mode_bg = tk.Label(self.left, bg='#525252', width=12)
		self.mode_bg.bind('<Button-1>', lambda e: self.change_mode())
		self.mode_lbl = tk.Label(self.left, text='Mode', font=('calibri', 12),
								 bg='#525252', fg='white')
		self.mode_stng = tk.Label(self.left, font=('calibri', 14),
								  bg='#525252', text=self.mode,
								  fg='#ff1212' if self.mode == 'Heat' else '#0062ff')
		self.mode_stng.bind('<Button-1>', lambda e: self.change_mode())
		
		self.fan_bg = tk.Label(self.left, bg='#525252', width=12)
		self.fan_lbl = tk.Label(self.left, text='Fan', font=('calibri', 12),
								bg='#525252', fg='white')
		self.fan_stng = tk.Label(self.left, font=('calibri', 14),
								 bg='#525252', fg='white',
								 text='On' if self.fan else 'Off')

		self.system_bg = tk.Label(self.left, bg='#525252', width=12)
		self.system_lbl = tk.Label(self.left, text='System', font=('calibri', 12),
								   bg='#525252', fg='white')
		self.system_stng = tk.Label(self.left, font=('calibri', 14),
									bg='#525252', fg='white',
									text=self.system)						

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

		self.curr_temp = self._thermostat.curr_temp
		self.desired_temp = self._thermostat.desired_temp

		self.curr_temp_lbl2 = tk.Label(self.middle, font=('calibri', 16),
									   bg='#525252', fg='white',
									   text='Current Temp')
		self.curr_temp_lbl = tk.Label(self.middle, font=('calibri', 40),
									  bg='#525252', fg='white',
									  text=str(self.curr_temp) + '°')
		self.desired_temp_lbl = tk.Label(self.middle, font=('calibri', 30), 
										 bg='#121212', fg='white', 
										 text=str(self.desired_temp) + '°')
		self.desired_temp_lbl2 = tk.Label(self.middle, font=('calibri', 14), 
										  bg='#121212', fg='white', 
										  text='Desired Temp')

		#temperature increment / decrement buttons
		self.temp_down = tk.Label(self.middle, font=('calibri', 35),
								  bg='#121212', fg='white', text='-')
		self.temp_down.bind('<Button-1>', lambda e: self.dec_temp())

		self.temp_up = tk.Label(self.middle, font=('calibri', 35),
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

	def change_mode(self):
		self.mode = self._thermostat.switch_mode()
		self.mode_stng.config(text=self.mode, fg='#ff1212' if self.mode == 'Heat' else '#0062ff')

# --------------------- End Helper Functions  ---------------------