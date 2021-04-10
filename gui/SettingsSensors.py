# SettingsSensors.py
# written by Harrison Noble

import tkinter as tk

class SettingsSensors(tk.Frame):
	'''SettingsSensors handles displaying the sensor outputs in the left side of the settings
	tab. Arguements are: 'parent' which is the frame object that creates this class, and 'thermostat' 
	which is the thermostat object created at the beginning of execution.'''
	
# --------------------- Init Function  ---------------------

	def __init__(self, parent, thermostat):
		#initialize frame and handle format
		tk.Frame.__init__(self, parent)
		self.config(bg='#525252')
		self.grid(row=1, column=0, columnspan = 2, sticky='nesw')
		self.rowconfigure((0, 1, 2, 3, 4), weight=1)
		self.columnconfigure((0, 1), weight=1)

		self._therm = thermostat

		#create and display temperature reading
		self.temp_sensor_lbl = tk.Label(self, text='Temperature Sensor',
										font=('calibri', 14), bg='#525252', fg='white')
		self.temp_sensor = tk.Label(self, text=str(self._therm.curr_temp) + '°',
									font=('calibri', 14), bg='#525252', fg='white')
		self.temp_sensor_lbl.grid(row=0, column=0, sticky='w', padx=(10, 0))
		self.temp_sensor.grid(row=0, column=1, sticky='e', padx=(0, 10))

		#create and display motion sensor reading
		self.motion_sensor_lbl = tk.Label(self, text='Motion Sensor',
										  font=('calibri', 14), bg='#525252', fg='white')
		self.motion_sensor = tk.Label(self, font=('calibri', 14),
									  text='Motion' if self._therm.motion else 'No Motion',
									  bg='#525252', fg='white')
		self.motion_sensor_lbl.grid(row=1, column=0, sticky='w', padx=(10, 0))
		self.motion_sensor.grid(row=1, column=1, sticky='e', padx=(0, 10))

		#create and display audio sensor reading
		self.audio_sensor_lbl = tk.Label(self, text='Audio Sensor',
										 font=('calibri', 14), bg='#525252', fg='white')
		self.audio_sensor = tk.Label(self, font=('calibri', 14),
									 text='Detected' if self._therm.sound else 'Not Detected',
									 bg='#525252', fg='white')
		self.audio_sensor_lbl.grid(row=2, column=0, sticky='w', padx=(10, 0))
		self.audio_sensor.grid(row=2, column=1, sticky='e', padx=(0, 10))

		#create and display camera reading
		self.camera_lbl = tk.Label(self, text='People Detected',
								   font=('calibri', 14), bg='#525252', fg='white')
		self.camera = tk.Label(self, text=str(self._therm.num_people),
							   font=('calibri', 14), bg='#525252', fg='white')
		self.camera_lbl.grid(row=3, column=0, sticky='w', padx=(10, 0))
		self.camera.grid(row=3, column=1, sticky='e', padx=(0, 10))

		#create and display room size reading
		self.room_size_lbl = tk.Label(self, text='Room Size Sensor',
									  font=('calibri', 14),
								   	  bg='#525252', fg='white')
		self.room_size_sensor = tk.Label(self, text=str(self._therm.room_size) + ' sq ft.',
										 font=('calibri', 14),
								   	  	 bg='#525252', fg='white')
		self.room_size_lbl.grid(row=4, column=0, sticky='w', padx=(10, 0))
		self.room_size_sensor.grid(row=4, column=1, sticky='e', padx=(0, 10))

		#variable used to stop sensors from updating
		self.stopper_sensors = None

# --------------------- End Init Function  ---------------------

# --------------------- Helper Functions  ---------------------

	def _update_sensors(self):
		'''function to update all sensor outputs except temp'''
		self.motion_sensor.config(text='Motion' if self._therm.motion else 'No Motion')
		self.audio_sensor.config(text='Detected' if self._therm.sound else 'Not Detected')
		self.camera.config(text=str(self._therm.num_people))
		self.room_size_sensor.config(text=str(self._therm.room_size) + ' sq ft.')

		self.stopper_sensors = self.after(200, self._update_sensors)

	def update_temp(self):
		'''function to update temperature output'''
		self.temp_sensor.config(text=str(self._therm.curr_temp) + '°')

	def stopper(self):
		'''function to stop update functions'''
		if self.stopper_sensors:
			self.after_cancel(self.stopper_sensors)
			self.stopper_sensors = None

	def starter(self):
		'''function to start all update functions'''
		self._update_sensors()

# --------------------- End Helper Functions  ---------------------
