# SettingsRight.py
# written by Harrison Noble

import tkinter as tk
import sys
import os
import time

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
		self.columnconfigure(0, weight=2)
		self.columnconfigure((1, 2), weight=1)
		self.rowconfigure((0, 1, 2, 3, 4), weight=1)

		self._therm = thermostat
		self._parent = parent

		#Thermostat power option
		self.pwr_option = tk.Label(self, text='Thermostat Power',
								   font=('calibri', 14),
								   bg='#525252', fg='white')
		self.pwr_option.grid(row=0, column=0, sticky='w', padx=(10, 0))

		self.on_btn = tk.Label(self, text='On', font=('calibri', 14),
								   bg='#cdcdcd', fg='#353535')
		self.on_btn.bind('<Button-1>', lambda e: self.toggle_power())
		self.off_btn = tk.Label(self, text='Off', font=('calibri', 14),
								   bg='#353535', fg='#cdcdcd')
		self.off_btn.bind('<Button-1>', lambda e: self.toggle_power())

		self.on_btn.grid(row=0, column=1, sticky='e', padx=(0, 4), ipadx=4)
		self.off_btn.grid(row=0, column=2, sticky='w', padx=(4, 0), ipadx=4)

		#reboot option
		self.reboot_option = tk.Label(self, text='Reboot Thermostat',
									  font=('calibri', 14),
									  bg='#525252', fg='white')
		self.reboot_option.grid(row=1, column=0, sticky='w', padx=(10, 0))

		self.reboot_btn = tk.Label(self,text='Reboot',
								   font=('calibri', 14),
								   bg='#cdcdcd', fg='#353535')
		self.reboot_btn.bind('<Button-1>', lambda e: self.reboot())
		self.reboot_btn.grid(row=1, column=1, columnspan=2, ipadx=4, padx=4)

		#max and min temp settings
		self.temp_range = tk.Label(self, text='Temp Range',
								   font=('calibri', 14),
								   bg='#525252', fg='white')
		self.temp_range.grid(row=2, column=0, sticky='w', padx=(10, 0))

		#fahrenheit or celcius setting
		self.temp_option = tk.Label(self, text='Temp Reading',
									font=('calibri', 14),
									bg='#525252', fg='white')
		self.temp_option.grid(row=3, column=0, sticky='w', padx=(10, 0))

		self.f_btn = tk.Label(self, text='F', font=('calibri', 14),
								   bg='#cdcdcd', fg='#353535')
		self.f_btn.bind('<Button-1>', lambda e: self.toggle_temp())
		self.c_btn = tk.Label(self, text='C', font=('calibri', 14),
								   bg='#353535', fg='#cdcdcd')
		self.c_btn.bind('<Button-1>', lambda e: self.toggle_temp())

		self.f_btn.grid(row=3, column=1, sticky='e', padx=(0, 4), ipadx=4)
		self.c_btn.grid(row=3, column=2, sticky='w', padx=(4, 0), ipadx=4)

		#adaptive or manual mode setting
		self.mode_option = tk.Label(self, text='Thermostat Mode',
									font=('calibri', 14),
									bg='#525252', fg='white')
		self.mode_option.grid(row=4, column=0, sticky='w', padx=(10, 0))

		self.adaptive_btn = tk.Label(self, text='Adaptive', font=('calibri', 14),
								   bg='#cdcdcd', fg='#353535')
		self.adaptive_btn.bind('<Button-1>', lambda e: self.toggle_mode())
		self.manual_btn = tk.Label(self, text='Manual', font=('calibri', 14),
								   bg='#353535', fg='#cdcdcd')
		self.manual_btn.bind('<Button-1>', lambda e: self.toggle_mode())

		self.adaptive_btn.grid(row=4, column=1, sticky='e', padx=(0, 2), ipadx=2)
		self.manual_btn.grid(row=4, column=2, sticky='w', padx=(2, 0), ipadx=2)

# --------------------- End Init Function  ---------------------

# --------------------- Helper Functions  ---------------------

	def toggle_power(self):
		if self._therm.is_on:
			self.off_btn.config(bg='#cdcdcd', fg='#353535')
			self.on_btn.config(bg='#353535', fg='#cdcdcd')
		else:
			self.on_btn.config(bg='#cdcdcd', fg='#353535')
			self.off_btn.config(bg='#353535', fg='#cdcdcd')
		self._therm.toggle_on()

	def reboot(self):
		print('Rebooting...')
		self._parent.stopper()
		time.sleep(2)
		os.execv(sys.executable, ['python3'] + sys.argv)

	def toggle_temp(self):
		if self._therm.degree == 'F':
			self.c_btn.config(bg='#cdcdcd', fg='#353535')
			self.f_btn.config(bg='#353535', fg='#cdcdcd')
		else:
			self.f_btn.config(bg='#cdcdcd', fg='#353535')
			self.c_btn.config(bg='#353535', fg='#cdcdcd')
		self._therm.toggle_degree()

	def toggle_mode(self):
		if self._therm.system == 'Adaptive':
			self.manual_btn.config(bg='#cdcdcd', fg='#353535')
			self.adaptive_btn.config(bg='#353535', fg='#cdcdcd')
		else:
			self.adaptive_btn.config(bg='#cdcdcd', fg='#353535')
			self.manual_btn.config(bg='#353535', fg='#cdcdcd')
		self._therm.toggle_system()

# --------------------- End Helper Functions  ---------------------