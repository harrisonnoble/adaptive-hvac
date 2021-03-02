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
		self.columnconfigure((0, 1), weight=1)
		self.rowconfigure((0, 1, 2, 3, 4), weight=1)

		self._therm = thermostat

		#Thermostat power option
		self.pwr_option = tk.Label(self, text='Thermostat Power',
								   font=('calibri', 14),
								   bg='#525252', fg='white')
		self.pwr_option.grid(row=0, column=0, sticky='w', padx=(10, 0))

		#reboot option
		self.reboot_option = tk.Label(self, text='Reboot Thermostat',
									  font=('calibri', 14),
									  bg='#525252', fg='white')
		self.reboot_option.grid(row=1, column=0, sticky='w', padx=(10, 0))

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

		#adaptive or manual mode setting
		self.temp_option = tk.Label(self, text='Thermostat Mode',
									font=('calibri', 14),
									bg='#525252', fg='white')
		self.temp_option.grid(row=4, column=0, sticky='w', padx=(10, 0))

# --------------------- End Init Function  ---------------------

# --------------------- Helper Functions  ---------------------

#TODO

# --------------------- End Helper Functions  ---------------------