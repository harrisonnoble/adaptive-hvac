# thermostat.py
# written by Harrison Noble

from gui.Gui import GUI
#import sensors

def start():
    '''Function to start execution of the thermostat.
    Creates and starts the main loop of the user interface'''

    app = GUI()
    app.title('Thermostat')
    app.mainloop()

# begin execution of the thermostat program
if __name__ == '__main__':
    start()