# gui.py
# written by Harrison Noble

from gui.Dashboard import Dashboard
from gui.Settings import Settings
import tkinter as tk

class Gui(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Dashboard(self)
        p2 = Settings(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)        

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)        

        b1.pack(side="left")
        b2.pack(side="left")        

        p1.show()

def start_gui():
    root = tk.Tk()
    main = Gui(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()