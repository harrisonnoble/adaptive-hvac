# SettingsLeft.py
# written by Harrison Noble

import tkinter as tk
from gui.SettingsSensors import SettingsSensors
from gui.SettingsCameras import SettingsCameras

class SettingsLeft(tk.Frame):
	'''SettingsLeft handles displaying the left side of the settings page. Arguements 
	are: 'parent' which is the frame object that creates this class, and 'thermostat' 
	which is the thermostat object created at the beginning of execution.'''
	
# --------------------- Init Function  ---------------------

	def __init__(self, parent, thermostat):
		#initialize frame and handle format
		tk.Frame.__init__(self, parent)
		self.config(bg='#525252')
		self.grid(row=1, column=0, rowspan=3, columnspan = 2, 
				  sticky='nesw', pady=(0, 20), padx=(15, 5))
		self.rowconfigure(0, weight=1)
		self.rowconfigure((1, 2, 3, 4, 5), weight=2)
		self.columnconfigure((0, 1), weight=1)

		#create toggle buttons between sensors and camera
		self.sensor_btn = tk.Label(self, text='Sensors', font=('calibri', 15),
								   bg='#cdcdcd', fg='#353535')
		self.sensor_btn.bind('<Button-1>', lambda e: self.toggle_view('Sensor'))
		self.camera_btn = tk.Label(self, text='Cameras', font=('calibri', 15),
								   bg='#353535', fg='#cdcdcd')
		self.camera_btn.bind('<Button-1>', lambda e: self.toggle_view('Camera'))

		#display toggle buttons
		self.sensor_btn.grid(row=0, column=0, sticky='ne', pady=(10, 0), padx=(0, 2))
		self.camera_btn.grid(row=0, column=1, sticky='nw', pady=(10, 0), padx=(2, 0))

		#create sensors and cameras frames
		self.sensors = SettingsSensors(self, thermostat)
		self.cameras = SettingsCameras(self, thermostat)

		self.toggle_view('Sensor')

# --------------------- End Init Function  ---------------------

# --------------------- Helper Functions  ---------------------

	def toggle_view(self, goto):
		if goto == 'Camera':
			self.camera_btn.config(bg='#cdcdcd', fg='#353535')
			self.sensor_btn.config(bg='#353535', fg='#cdcdcd')
			self.cameras.update_img()
			self.cameras.tkraise()
		else:
			self.sensor_btn.config(bg='#cdcdcd', fg='#353535')
			self.camera_btn.config(bg='#353535', fg='#cdcdcd')
			self.cameras.stop_update()
			self.sensors.tkraise()

# --------------------- End Helper Functions  ---------------------
