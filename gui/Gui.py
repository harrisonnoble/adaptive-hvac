# Gui.py
# written by Harrison Noble

from gui.Dashboard import Dashboard
from gui.Settings import Settings
import tkinter as tk
import sys

class Gui(tk.Tk): 
	'''GUI class handles the creation and toggling between the settings page 
	and dashboard page. This is the parent class for both pages. The arguement
	is 'thermostat' which is the thermostat object created at the beginning of 
	execution.'''

# --------------------- Init Function  ---------------------   

	def __init__(self, thermostat): 
		# create the container window and set the size
		tk.Tk.__init__(self)
		container = tk.Frame(self)  

		# if -f arguement, run in fullscreen mode
		if len(sys.argv) == 2 and sys.argv[1] == '-f':
			self.attributes('-fullscreen', True)
			self.bind('<Escape>', lambda e: self.attributes('-fullscreen', False))
		else:
			self.geometry('800x480')

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

		#call the thermostat algorithm function every second
		self._therm = thermostat
		self.algo_stopper = self.after(1000, self._run_algorithm)

# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  ---------------------  

	def _run_algorithm(self):
		self._therm.algorithm()
		self.algo_stopper = self.after(1000, self._run_algorithm)

	def show_dashboard(self):
		'''Toggle to the main dashboard'''
		#stop update functions in settings first
		self.frame[Settings].stopper()

		frame = self.frame[Dashboard]
		frame.starter()
		frame.tkraise()
	
	def show_settings(self): 
		'''Toggle to the settings page'''
		#stop update functions in dashboard first
		self.frame[Dashboard].stopper()

		frame = self.frame[Settings] 
		frame.starter()
		frame.tkraise()

# --------------------- End Helper Functions  ---------------------  