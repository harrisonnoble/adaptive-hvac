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
		self.grid(row=1, column=0, rowspan=5, columnspan = 2, sticky='nesw')
		self.rowconfigure((0, 1, 2, 3), weight=1)
		self.columnconfigure((0, 1), weight=1)

		self._therm = thermostat

		#create and display temperature reading
		self.temp_sensor_lbl = tk.Label(self, text='Temperature Sensor',
										font=('calibri', 18), bg='#525252', fg='white')
		self.temp_sensor = tk.Label(self, text=str(self._therm.curr_temp) + '°',
									font=('calibri', 18), bg='#525252', fg='white')
		self.temp_sensor_lbl.grid(row=0, column=0, sticky='nw', padx=10)
		self.temp_sensor.grid(row=0, column=1, sticky='ne', padx=10)

		#create and display motion sensor reading
		self.motion_sensor_lbl = tk.Label(self, text='Motion Sensor',
										  font=('calibri', 18), bg='#525252', fg='white')
		self.motion_sensor = tk.Label(self, font=('calibri', 18),
									  text='Motion' if self._therm.motion else 'No Motion',
									  bg='#525252', fg='white')
		self.motion_sensor_lbl.grid(row=1, column=0, sticky='nw', padx=10)
		self.motion_sensor.grid(row=1, column=1, sticky='ne', padx=10)

		#create and display audio sensor reading
		self.audio_sensor_lbl = tk.Label(self, text='Audio Sensor',
										 font=('calibri', 18), bg='#525252', fg='white')
		self.audio_sensor = tk.Label(self, font=('calibri', 18),
									 text='Detected' if self._therm.sound else 'Not Detected',
									 bg='#525252', fg='white')
		self.audio_sensor_lbl.grid(row=2, column=0, sticky='nw', padx=10)
		self.audio_sensor.grid(row=2, column=1, sticky='ne', padx=10)

		#create and display camera reading
		self.camera_lbl = tk.Label(self, text='Number of People Detected',
								   font=('calibri', 18), bg='#525252', fg='white')
		self.camera = tk.Label(self, text=str(self._therm.num_people),
							   font=('calibri', 18), bg='#525252', fg='white')
		self.camera_lbl.grid(row=3, column=0, sticky='nw', padx=10)
		self.camera.grid(row=3, column=1, sticky='ne', padx=10)

# --------------------- End Init Function  ---------------------

# --------------------- Helper Functions  ---------------------

#TODO

# --------------------- End Helper Functions  ---------------------
