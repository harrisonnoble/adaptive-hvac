# Gui.py
# written by Harrison Noble

from gui.Dashboard import Dashboard
from gui.Settings import Settings
import tkinter as tk

class GUI(tk.Tk): 
	'''GUI class handles the creation and toggling between the settings page 
	and dashboard page. This is the parent class for both pages. The arguement
	is 'thermostat' which is the thermostat object created at the beginning of 
	execution.'''

# --------------------- Init Function  ---------------------   

	def __init__(self, thermostat): 
		# create the container window and set the size
		tk.Tk.__init__(self)  
		container = tk.Frame(self)  
		tk.Tk.geometry(self,'800x480')

		# formatting for the window
		container.pack(side='top', fill='both', expand = True) 
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		#create the dashboard and settings page and store in frame
		self.frame = {}
		for F in (Dashboard, Settings):
			frame = F(container, self, thermostat)
			self.frame[F] = frame
			frame.grid(row = 0, column = 0, sticky = "nsew") 

		#initially display the main dashboard
		self.show_dashboard()

# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  ---------------------  

	def show_dashboard(self):
		'''Toggle to the main dashboard'''
		frame = self.frame[Dashboard]    
		frame.tkraise()
	
	def show_settings(self): 
		'''Toggle to the settings page'''
		frame = self.frame[Settings] 
		frame.tkraise()

# --------------------- End Helper Functions  ---------------------  