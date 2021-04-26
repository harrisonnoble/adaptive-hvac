# Gui.py
# written by Harrison Noble

from gui import Dashboard, Settings
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

		self.protocol('WM_DELETE_WINDOW', self._on_close)

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

		#create the dashboard and settings page
		self.dashboard = Dashboard(container, self, thermostat)
		self.dashboard.grid(row = 0, column = 0, sticky = "nsew")

		self.settings = Settings(container, self, thermostat)
		self.settings.grid(row = 0, column = 0, sticky = "nsew") 

		#initially display the main dashboard
		self.show_dashboard()

		#call the thermostat algorithm function every 0.75 seconds
		self._therm = thermostat
		self._algo_stopper = self.after(750, self._run_algorithm)

# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  ---------------------  

	def _on_close(self):
		'''Function to run when program is closed'''
		if self._algo_stopper:
			self.after_cancel(self._algo_stopper)
			self._algo_stopper = None
		self._therm.save()

	def _run_algorithm(self):
		'''Function that calls the thermostat algorithm'''
		self._therm.algorithm()
		self._algo_stopper = self.after(750, self._run_algorithm)

	def show_dashboard(self):
		'''Toggle to the main dashboard'''
		self.settings.stopper()
		self.dashboard.starter()
		self.dashboard.tkraise()
	
	def show_settings(self): 
		'''Toggle to the settings page'''
		self.dashboard.stopper()
		self.settings.starter()
		self.settings.tkraise()

# --------------------- End Helper Functions  ---------------------  