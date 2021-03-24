# SettingsCameras.py
# written by Harrison Noble

import tkinter as tk
from PIL import Image, ImageTk

class SettingsCameras(tk.Frame):
	'''SettingsCameras handles displaying the camera outputs in the left side of the settings
	tab. Arguements are: 'parent' which is the frame object that creates this class, and 'thermostat' 
	which is the thermostat object created at the beginning of execution.'''
	
# --------------------- Init Function  ---------------------

	def __init__(self, parent, thermostat):
		#initialize frame and handle format
		tk.Frame.__init__(self, parent)
		self.config(bg='#525252')
		self.grid(row=1, column=0, rowspan=6, columnspan = 2, sticky='nesw')
		self.rowconfigure((0, 1, 2, 3, 4), weight=1)
		self.columnconfigure((0, 1), weight=1)

		#store thermostat object
		self._therm = thermostat

		#add title for camera and display camera output
		self.cam_title = tk.Label(self, text='Camera', font=('calibri', 12),
								  bg='#525252', fg='white')
		self.cam_title.grid(row=0, column=0, columnspan=2, sticky='n')

		self.picture = ImageTk.PhotoImage(image= Image.fromarray(self._therm.get_img()))
		self.cam_img = tk.Label(self, image=self.picture)
		self.cam_img.grid(row=0, column=0, rowspan=2, columnspan=2)

		#add title for thermal camera and display output
		self.therm_title = tk.Label(self, text='Thermal Camera', font=('calibri', 12),
								    bg='#525252', fg='white')
		self.therm_title.grid(row=2, column=0, columnspan=2, sticky='n')

		#TODO: Thermal camera implementation
		
		#variable used to stop camera outputs from updating
		self.stopper_img = None

# --------------------- End Init Function  ---------------------

# --------------------- Helper Functions  ---------------------

	def update_imgs(self):
		#get image from camera and display on the page
		self.picture = ImageTk.PhotoImage(image=Image.fromarray(self._therm.get_img()))
		self.cam_img.config(image=self.picture)

		#TODO: write code to update thermal camera output

		self.stopper_img = self.cam_img.after(500, self.update_imgs)

	def stopper(self):
		#stop updating camera outputs
		if self.stopper_img:
			self.cam_img.after_cancel(self.stopper_img)
			self.stopper_img = None

	def starter(self):
		self.update_imgs()

# --------------------- End Helper Functions  ---------------------