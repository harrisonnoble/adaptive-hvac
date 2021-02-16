# gui.py
# written by Harrison Noble

from gui.Dashboard import Dashboard
from gui.Settings import Settings
import tkinter as tk

class GUI(tk.Tk):  

	def __init__(self, thermostat, *args, **kwargs): 
		# create the container window and set the size
		tk.Tk.__init__(self, *args, **kwargs)  
		container = tk.Frame(self)  
		tk.Tk.geometry(self,'800x480')

		self.thermostat = thermostat

		# formatting for the window
		container.pack(side='top', fill='both', expand = True )     
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		self.frame = {}

		#create the dashboard and settings page and store in frame
		for F in (Dashboard, Settings):
			frame = F(container, self)
			self.frame[F] = frame
			frame.grid(row = 0, column = 0, sticky = "nsew") 

		#initially display the main dashboard
		self.show_dashboard()

	def show_dashboard(self):
		'''Toggle to the main dashboard'''
		frame = self.frame[Dashboard]    
		frame.tkraise()
	
	def show_settings(self): 
		'''Toggle to the settings page'''
		frame = self.frame[Settings] 
		frame.tkraise()