# SettingsLeft.py
# written by Harrison Noble

import tkinter as tk
from gui.SettingsSensors import SettingsSensors
from gui.SettingsCameras import SettingsCameras

class SettingsLeft(tk.Frame):
	'''SettingsLeft handles displaying the left side of the settings page. Arguements are: 'parent' which is the frame object 
	that creates this class, and 'thermostat' which is the thermostat object created at the beginning of execution.'''
	
# --------------------- Init Function  ---------------------

	def __init__(self, parent, thermostat):
		#initialize frame and handle format
		tk.Frame.__init__(self, parent)
		self.config(bg='#525252')
		self.grid(row=1, column=0, columnspan = 2, sticky='nesw', pady=(0, 20), padx=(15, 5))
		self.rowconfigure(0, weight=1)
		self.rowconfigure(1, weight=10)
		self.columnconfigure((0, 1), weight=1)

		self._therm = thermostat

		#create toggle buttons between sensors and camera
		self.sensor_btn = tk.Label(self, text='Sensors', font=('calibri', 14),
								   bg='#cdcdcd', fg='#353535')
		self.sensor_btn.bind('<Button-1>', lambda e: self._show_sensors())
		self.sensor_btn.grid(row=0, column=0, sticky='ne', pady=(10, 5), padx=(0, 4), ipadx=4)

		self.camera_btn = tk.Label(self, text='Cameras', font=('calibri', 14),
								   bg='#353535', fg='#cdcdcd')
		self.camera_btn.bind('<Button-1>', lambda e: self._show_cameras())
		self.camera_btn.grid(row=0, column=1, sticky='nw', pady=(10, 5), padx=(4, 0), ipadx=4)

		#create sensors and cameras frames
		self.sensors = SettingsSensors(self, thermostat)
		self.cameras = SettingsCameras(self, thermostat)

		self._on_sensors = True
		self._show_sensors()

# --------------------- End Init Function  ---------------------

# --------------------- Helper Functions  ---------------------

	def _show_cameras(self):
		'''display camera page and stop the sensor page update function'''
		self.camera_btn.config(bg='#cdcdcd', fg='#353535')
		self.sensor_btn.config(bg='#353535', fg='#cdcdcd')

		self.sensors.stopper()
		self._therm.camera.streaming_img = True
		self.cameras.starter()
		self.cameras.tkraise()

		self._on_sensors = False
	
	def _show_sensors(self):
		'''display sensor page and stop the camera page update function'''
		self.sensor_btn.config(bg='#cdcdcd', fg='#353535')
		self.camera_btn.config(bg='#353535', fg='#cdcdcd')

		self.cameras.stopper()
		self._therm.camera.streaming_img = False
		self.sensors.starter()
		self.sensors.tkraise()

		self._on_sensors = True

	def update_temp_output(self):
		'''Intermediary function to update temperature label in sensor page'''
		if self._on_sensors:
			self.sensors.update_temp()

	def stopper(self):
		'''stop all update functions'''
		self.cameras.stopper()
		self.sensors.stopper()
		self._therm.camera.streaming_img = False

	def starter(self):
		'''start all update functions'''
		if not self._on_sensors:
			self.sensors.stopper()
			self._therm.camera.streaming_img = True
			self.cameras.starter()
		else:
			self.cameras.stopper()
			self._therm.camera.streaming_img = False
			self.sensors.starter()

# --------------------- End Helper Functions  ---------------------
