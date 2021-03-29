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
		self.sensor_btn = tk.Label(self, text='Sensors', font=('calibri', 12),
								   bg='#cdcdcd', fg='#353535')
		self.sensor_btn.bind('<Button-1>', lambda e: self.toggle_view('Sensor'))
		self.camera_btn = tk.Label(self, text='Cameras', font=('calibri', 12),
								   bg='#353535', fg='#cdcdcd')
		self.camera_btn.bind('<Button-1>', lambda e: self.toggle_view('Camera'))

		#display toggle buttons
		self.sensor_btn.grid(row=0, column=0, sticky='ne', pady=(10, 0), padx=(0, 4), ipadx=4)
		self.camera_btn.grid(row=0, column=1, sticky='nw', pady=(10, 0), padx=(4, 0), ipadx=4)

		#create sensors and cameras frames
		self.sensors = SettingsSensors(self, thermostat)
		self.cameras = SettingsCameras(self, thermostat)

		self._therm = thermostat

		self._view = 'Sensor'
		self.toggle_view('Sensor')

# --------------------- End Init Function  ---------------------

# --------------------- Helper Functions  ---------------------

	def toggle_view(self, goto):
		'''display camera page or sensor page and stop respective update function'''
		if goto == 'Camera':
			self.camera_btn.config(bg='#cdcdcd', fg='#353535')
			self.sensor_btn.config(bg='#353535', fg='#cdcdcd')
			self.sensors.stopper()
			self._therm.camera.streaming_img = True
			self.cameras.starter()
			self.cameras.tkraise()

			self._view = goto
		else:
			self.sensor_btn.config(bg='#cdcdcd', fg='#353535')
			self.camera_btn.config(bg='#353535', fg='#cdcdcd')
			self.cameras.stopper()
			self._therm.camera.streaming_img = False
			self.sensors.starter()
			self.sensors.tkraise()

			self._view = goto

	def stopper(self):
		'''stop all update functions'''
		self.cameras.stopper()
		self.sensors.stopper()
		self._therm.camera.streaming_img = False

	def starter(self):
		'''start all update functions'''
		if self._view == 'Camera':
			self.sensors.stopper()
			self._therm.camera.streaming_img = True
			self.cameras.starter()
		else:
			self.cameras.stopper()
			self._therm.camera.streaming_img = False
			self.sensors.starter()

	def update_temp_output(self):
		'''Intermediary function to update temperature label in sensor page'''
		if self._view == 'Sensor':
			self.sensors.update_temp_degree()

# --------------------- End Helper Functions  ---------------------
