# settings.py
# written by Harrison Noble

import tkinter as tk
from gui.Page import Page

class Settings(Page):

    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is settings")
       label.pack(side="top", fill="both", expand=True)