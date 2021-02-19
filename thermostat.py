# thermostat.py
# written by Harrison Noble
#THIS IS THE MAIN ENTRYPOINT FOR THE PROGRAM

from gui.Gui import GUI
import sensors.Sensors as sensors

class Thermostat:
    '''Thermostat class creates UI and all sensors. This is the main
    entry point for program. To begin program please run 'python3 thermostat.py'.
    After initializing all needed components, program will begin the execution
    of the main loop which handles all UI and thermostat logic'''

# --------------------- Init Function  ---------------------  

    def __init__(self):

        #Initialize all sensors
        self.camera = sensors.Camera()
        self.motion_sensor = sensors.MotionSensor()
        self.temp_sensor = sensors.TempSensor()
        self.therm_camera = sensors.ThermalCamera()

        #initialize all needed variables for thermostat execution
        self._min_temp = 50
        self._max_temp = 85
        self._curr_temp = self.temp_sensor.get_temp() or 0
        self._desired_temp = self._min_temp
        self._num_people = 0
        self._motion = False
        self._sound = False
        self._mode = 'Heat'
        self._fan = 0
        self._system = 'Adaptive'

        self._app = GUI(self)
        self._app.title('Thermostat')

        self.start()

# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  ---------------------  

    def start(self):
        '''Function to start execution of the thermostat.
        Starts the main loop of the user interface'''
        self._app.mainloop()

    #getters and setters
    @property
    def min_temp(self):
        return self._min_temp

    @min_temp.setter
    def min_temp(self, t):
        self._min_temp = t

    @property
    def max_temp(self):
        return self._max_temp
    
    @max_temp.setter
    def max_temp(self, t):
        self._max_temp = t

    @property
    def curr_temp(self):
        return self._curr_temp

    @property
    def desired_temp(self):
        return self._desired_temp
    
    @desired_temp.setter
    def desired_temp(self, t):
        self._desired_temp = t

    @property
    def num_people(self):
        return self._num_people

    @property
    def motion(self):
        return self._motion
    
    @property
    def sound(self):
        return self._sound

    @property
    def mode(self):
        return self._mode

    @property
    def fan(self):
        return self._fan
    
    @property
    def system(self):
        return self._system

    #functions to update variables
    def update_curr_temp(self):
        '''Reads temperature sensor, updates curr_temp variable, and returns value'''
        self._curr_temp = self.temp_sensor.get_temp()
        return self._curr_temp

    def inc_desired_temp(self):
        '''Increments desired temperature by 1 degree'''
        if self._desired_temp < self._max_temp:
            self._desired_temp += 1
        return self._desired_temp
    
    def dec_desired_temp(self):
        '''Decrements desired temperature by 1 degree'''
        if self._desired_temp > self._min_temp:
            self._desired_temp -= 1
        return self._desired_temp

    def switch_mode(self):
        '''Toggles thermostat between 'Heat' and 'Cool' modes and returns value'''
        self._mode = 'Heat' if self._mode == 'Cool' else 'Cool'
        return self._mode

    def switch_system(self):
        '''Toggles system between 'Adaptive' and 'Manual' modes and returns value'''
        self._system = 'Adaptive' if self._system == 'Manual' else 'Manual'
    


# --------------------- End Helper Functions  ---------------------  

# --------------------- Entry Point  ---------------------  

# begin execution of the thermostat program
if __name__ == '__main__':
    thermostat = Thermostat()