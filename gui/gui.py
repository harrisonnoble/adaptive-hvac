# gui.py
# written by Harrison Noble

from gui.Dashboard import Dashboard
from gui.Settings import Settings
import tkinter as tk

class GUI(tk.Tk):  

	def __init__(self, *args, **kwargs):  
		tk.Tk.__init__(self, *args, **kwargs)
		#tk.Tk.iconbitmap(self,default="ico_image.ico")  

		container = tk.Frame(self)  
		tk.Tk.geometry(self,'250x250')  
		container.pack(side='top', fill='both', expand = True )     
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		self.frame = {}

		for F in (Dashboard, Settings):
			frame = F(container, self)
			self.frame[F] = frame
			frame.grid(row = 0, column = 0, sticky = "nsew") 

		self.show_dashboard()

	def show_dashboard(self):
		frame = self.frame[Dashboard]    
		frame.tkraise()
	
	def show_settings(self): 
		frame = self.frame[Settings] 
		frame.tkraise()