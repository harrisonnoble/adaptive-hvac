# thermostat.py
# written by Harrison Noble

from gui.Gui import GUI
# from sensors.Camera import Camera
# from sensors.MotionSensor import MotionSensor
# from sensors.TempSensor import TempSensor
# from sensors.ThermCamera import ThermalCamera
import sensors.Sensors as sensors

class Thermostat:
    def __init__(self):
        self.app = GUI(self)
        self.app.title('Thermostat')

        self.camera = sensors.Camera()
        self.motion_sensor = sensors.MotionSensor()
        self.temp_sensor = sensors.TempSensor()
        self.therm_camera = sensors.ThermalCamera()

    def start(self):
        '''Function to start execution of the thermostat.
        Starts the main loop of the user interface'''

        self.app.mainloop()


# begin execution of the thermostat program
if __name__ == '__main__':
    thermo = Thermostat()
    thermo.start()