# settings.py
# written by Harrison Noble

import tkinter as tk
from time import strftime
import os

class Settings(tk.Frame):    

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.config(bg='#121212')
		for i in range(0, 4):
			self.rowconfigure(i, weight=1)
			self.columnconfigure(i, weight=1, min='200')

		#get back image
		curr_path = os.path.dirname(os.path.realpath(__file__))
		self.image = tk.PhotoImage(file=curr_path + '/imgs/back.png')
		self.image = self.image.subsample(4, 4)

		#create a label with the back image and bind show_dashboard function
		self.toggle_btn = tk.Label(self, image=self.image, borderwidth=0)
		self.toggle_btn.bind('<Button-1>', lambda e: controller.show_dashboard())

		self.time_label = tk.Label(self, font=('calibri', 35),
									background='#121212',
									foreground='white')

		#display all components
		self.toggle_btn.grid(column=0, row=0, sticky='nw', padx=10, pady=5)
		self.time_label.grid(column=1, row=0, sticky='new', columnspan=2)
		
		#call the update time function
		self.update_time()

	def update_time(self):
		'''Function to update the displayed time every 30 seconds'''
		t = strftime('%-I:%M %p')
		self.time_label.config(text=t)
		self.time_label.after(30000, self.update_time)