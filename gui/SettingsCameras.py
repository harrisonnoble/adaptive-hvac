# SettingsCameras.py
# written by Harrison Noble

import tkinter as tk
from PIL import Image, ImageTk

class SettingsCameras(tk.Frame):
	'''SettingsCameras handles displaying the camera outputs in the left side of the settings tab. Arguements are: 'parent' which 
	is the frame object that creates this class, and 'thermostat' which is the thermostat object created at the beginning of execution.'''
	
# --------------------- Init Function  ---------------------

	def __init__(self, parent, thermostat):
		#initialize frame and handle format
		tk.Frame.__init__(self, parent)
		self.config(bg='#525252')
		self.grid(row=1, column=0, columnspan = 2, sticky='nesw')
		self.rowconfigure((0, 1), weight=1)
		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=2)

		#store thermostat object
		self._therm = thermostat

		#add title for camera and display camera output
		self.cam_title = tk.Label(self, text='Camera', font=('calibri', 14), bg='#525252', fg='white')
		self.cam_title.grid(row=0, column=0, sticky='w', padx=(10, 0))

		self.cam_img = tk.Label(self)
		try:
			self.picture = ImageTk.PhotoImage(image=Image.fromarray(self._therm.get_img()))
			self.cam_img.config(image=self.picture)
		except:
			pass
		self.cam_img.grid(row=0, column=1, padx=(0, 10), pady=10)

		#add title for thermal camera and display output
		self.therm_title = tk.Label(self, text='Thermal Camera', font=('calibri', 14), bg='#525252', fg='white')
		self.therm_title.grid(row=1, column=0, sticky='w', padx=(10, 0))

		self.therm_img = tk.Label(self)
		try:
			self.therm_picture = ImageTk.PhotoImage(image=Image.fromarray(self._therm.get_therm_img()))
			self.therm_img.config(image=self.therm_picture)
		except:
			pass
		self.therm_img.grid(row=1, column=1, pady=10)
		
		#variable used to stop camera outputs from updating
		self._stopper_img = None

# --------------------- End Init Function  ---------------------

# --------------------- Helper Functions  ---------------------

	def _update_imgs(self):
		'''get image from camera/thermal camera and display on the page'''
		try:
			self.picture = ImageTk.PhotoImage(image=Image.fromarray(self._therm.get_img()))
			self.cam_img.config(image=self.picture)
		except:
			pass

		try:
			self.therm_picture = ImageTk.PhotoImage(image=Image.fromarray(self._therm.get_therm_img()))
			self.therm_img.config(image=self.therm_picture)
		except:
			pass

		self._stopper_img = self.after(500, self._update_imgs)

	def stopper(self):
		'''function to stop updating camera outputs'''
		if self._stopper_img:
			self.after_cancel(self._stopper_img)
			self._stopper_img = None

	def starter(self):
		'''function to start camera update function'''
		self._update_imgs()

# --------------------- End Helper Functions  ---------------------