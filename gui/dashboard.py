# dashboard.py
# written by Harrison Noble

import tkinter as tk
from time import strftime
import os

class Dashboard(tk.Frame):    

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)   
		self.config(bg='#121212')
		for i in range(0, 4):
			self.rowconfigure(i, weight=3)
			self.columnconfigure(i, weight=3, min='200')

		#get settings image
		curr_path = os.path.dirname(os.path.realpath(__file__))
		self.image = tk.PhotoImage(file=curr_path + '/imgs/settings.png')
		self.image = self.image.subsample(4, 4)

		#create a label with the settings image and bind show_settings function
		self.toggle_btn = tk.Label(self, image=self.image, borderwidth=0)
		self.toggle_btn.bind('<Button-1>', lambda e: controller.show_settings())

		#create label for the time
		self.time_lbl = tk.Label(self, font=('calibri', 35), bg='#121212', fg='white')

		#create variables for temperature
		self.curr_temp_lbl = tk.Label(self, font=('calibri', 40), bg='#525252', fg='white')
		self.curr_temp = 0
		self.desired_temp_lbl = tk.Label(self, font=('calibri', 30), bg='#121212', fg='white')
		self.desired_temp = 0

		#display all components
		self.time_lbl.grid(column=1, row=0, sticky='new', columnspan=2)
		self.toggle_btn.grid(column=3, row=0, sticky='ne', padx=10, pady=5)

		self.curr_temp_lbl.grid(column=1, row=1, columnspan=2)
		self.desired_temp_lbl.grid(column=1, row=2, columnspan=2)

		#call functions to update values
		self.update_time()
		self.update_curr_temp(0)
		self.update_desired_temp(0)

	def update_time(self):
		'''Function to update the displayed time every 30 seconds'''
		t = strftime('%-I:%M %p')
		self.time_lbl.config(text=t)
		self.time_lbl.after(30000, self.update_time)

	def update_curr_temp(self, temp):
		'''Function to update current temperature label'''
		self.curr_temp = temp
		self.curr_temp_lbl.config(text=str(self.curr_temp) + '°')
		pass

	def update_desired_temp(self, temp):
		'''Function to update desired temperature label'''
		self.desired_temp = temp
		self.desired_temp_lbl.config(text=str(self.desired_temp) + '°')
		pass