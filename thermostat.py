# thermostat.py
# written by Harrison Noble

from gui.Gui import GUI

class Thermostat:
    def __init__(self):
        self.app = GUI(self)
        self.app.title('Thermostat')

    def start(self):
        '''Function to start execution of the thermostat.
        Starts the main loop of the user interface'''

        self.app.mainloop()


# begin execution of the thermostat program
if __name__ == '__main__':
    thermo = Thermostat()
    thermo.start()