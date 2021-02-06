# dashboard.py
# written by Harrison Noble

import tkinter as tk

class Dashboard(tk.Frame):    

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)   
		label = tk.Label(self, text="Dashboard")
		label.pack(pady=10,padx=10)

		button1 = tk.Button(self, text = "To Settings",
			command = lambda: controller.show_settings(), width = 25, height = 1)
		button1.pack()