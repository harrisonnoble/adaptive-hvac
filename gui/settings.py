# settings.py
# written by Harrison Noble

import tkinter as tk

class Settings(tk.Frame):    

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)   
		l = tk.Label(self, text="Settings")
		l.pack(pady=10,padx=10)
        
		button1 = tk.Button(self, text = "To Dashboard",
			command = lambda: controller.show_dashboard(), width = 25, height = 1)
		button1.pack()

		self.label = tk.Label(self, text='nothing')
		self.label.pack()
		self.count = 0
		self.update_label()

	def update_label(self):
		self.label.configure(text = 'count: {}'.format(self.count))
		# self.label.after(1, self.update_label) # call this method again in 1,000 milliseconds
		self.count += 10
		# print(self.count)