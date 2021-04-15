#!/usr/bin/python3

# thermostat.py
# written by Harrison Noble
#THIS IS THE MAIN ENTRYPOINT FOR THE PROGRAM

from gui.Gui import Gui
from sensors.AudioSensor import AudioSensor
from sensors.Camera import Camera
from sensors.MotionSensor import MotionSensor
from sensors.TempSensor import TempSensor
from sensors.ThermCamera import ThermalCamera
from sensors.DistanceSensor import DistanceSensor
from sensors.LEDs import LEDs
import configparser
import os

class Thermostat:
    '''Thermostat class creates UI and all sensors. This is the main
    entry point for program. To begin program please run 'python3 thermostat.py'.
    After initializing all needed components, program will begin the execution
    of the main loop which handles all UI and thermostat logic'''

# --------------------- Init Function  ---------------------  

    def __init__(self):
        #first read in the config file
        self._cfg = self._read_config()

        #Initialize all sensors & cameras
        self.audio_sensor = AudioSensor()
        self.motion_sensor = MotionSensor()
        self.temp_sensor = TempSensor(self._cfg.get('thermostat', 'degree'))
        self.therm_camera = ThermalCamera()
        self.distance_sensor = DistanceSensor()
        self.camera = Camera()
        self.leds = LEDs()

        #initialize all needed variables for thermostat execution
        self._is_on = self._cfg.getboolean('thermostat', 'on', fallback=str(True))
        self._degrees = self.temp_sensor.mode
        self._min_temp = self._cfg.getint('thermostat', 'min_temp')
        self._max_temp = self._cfg.getint('thermostat', 'max_temp')
        self._curr_temp = self.temp_sensor.temp
        self._desired_temp = self._cfg.getint('thermostat', 'desired_temp')
        self._num_people = 0
        self._motion = self.motion_sensor.motion
        self._room_size = self.distance_sensor.distance ** 2
        self._sound = self.audio_sensor.sound
        self._is_heating = self._cfg.getboolean('thermostat', 'heat', fallback=str(True))
        self._fan = self._cfg.getboolean('thermostat', 'fan', fallback=str(False))
        self._system = self._cfg.get('thermostat', 'system')

        #bind motion/no motion detection functions
        self.motion_sensor.set_motion_func(self._motion_func)
        self.motion_sensor.set_no_motion_func(self._no_motion_func)

        #bind sound detection to updating sound variable
        self.audio_sensor.set_sound_func(self._sound_func)

        #create GUI and start
        self._app = Gui(self)
        self._app.title('Thermostat')
        self._app.mainloop()

# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  ---------------------  

    def _motion_func(self):
        '''function that runs when motion is detected, updates number of people
        and sets motion value to true'''
        self._motion = self.motion_sensor.motion
        self.update_num_people()

    def _no_motion_func(self):
        '''function to run when motion is not detected, updates motion value to false'''
        self._motion = self.motion_sensor.motion

    def _sound_func(self):
        '''function to run when audio is detectued, updates sound variable'''
        self._sound = self.audio_sensor.sound

    def _read_config(self):
        '''Function to get configurable variables from config.ini file'''
        curr_path = os.path.dirname(os.path.realpath(__file__))
        cfg = configparser.ConfigParser(allow_no_value=True)
        try:
            cfg.read(curr_path + '/config.cfg')
        except:
            #error handling
            cfg.add_section('thermostat')
            self._cfg.set('thermostat', 'on', str(True))
            self._cfg.set('thermostat', 'degree', 'F')
            self._cfg.set('thermostat', 'min_temp', str(50))
            self._cfg.set('thermostat', 'max_temp', str(85))
            self._cfg.set('thermostat', 'desired_temp', str(70))
            self._cfg.set('thermostat', 'heat', str(True))
            self._cfg.set('thermostat', 'fan', str(False))
            self._cfg.set('thermostat', 'system', 'Adaptive')
        
        #return config
        return cfg

    def write_config(self):
        '''Function to write configurable variables to the config.ini file'''
        #update config variables
        self._cfg.set('thermostat', 'on', str(self._is_on))
        self._cfg.set('thermostat', 'degree', str(self._degrees))
        self._cfg.set('thermostat', 'min_temp', str(self._min_temp))
        self._cfg.set('thermostat', 'max_temp', str(self._max_temp))
        self._cfg.set('thermostat', 'desired_temp', str(self._desired_temp))
        self._cfg.set('thermostat', 'heat', str(self._is_heating))
        self._cfg.set('thermostat', 'fan', str(self._fan))
        self._cfg.set('thermostat', 'system', str(self._system))

        #write to config
        with open('config.cfg', 'w') as configfile:
            configfile.write('; DO NOT EDIT\n')
            self._cfg.write(configfile)

    def toggle_on(self):
        '''function to toggle thermostat power (returns true if on, false if off)'''
        self._is_on = not self._is_on
        return self._is_on

    def toggle_degree(self):
        '''function to toggle between C and F'''
        self._degrees = self.temp_sensor.toggle_mode()
        self.update_curr_temp()
        self.update_temps()
        return self._degrees

    def update_curr_temp(self):
        '''function to update temperature value'''
        self._curr_temp = self.temp_sensor.temp
        return self._curr_temp

    def update_num_people(self):
        '''function to detect number of people and update value'''
        self._num_people = self.camera.num_people
        return self._num_people

    def toggle_fan(self):
        '''function to toggle fan on and off, returns true if fan is on, false if fan is off'''
        self._fan = False if self._fan else True
        return self._fan

    def toggle_system(self):
        '''function to switch between adaptive and manual mode, returns the current mode after toggling'''
        self._system = 'Adaptive' if self._system == 'Manual' else 'Manual'
        return self._system

    def update_temps(self):
        '''function to update min temp, max temp, and desired temp based on degree'''
        if self._degrees == 'C': #F to C
            self._min_temp = round((self._min_temp - 32) * (5/9))
            self._max_temp = round((self._max_temp - 32) * (5/9))
            self._desired_temp = round((self._desired_temp - 32) * (5/9))
        else: #C to F
            self._min_temp = round((self._min_temp * 1.8) + 32)
            self._max_temp = round((self._max_temp * 1.8) + 32)
            self._desired_temp = round((self._desired_temp * 1.8) + 32)

    def update_curr_temp(self):
        '''Reads temperature sensor, updates curr_temp variable, and returns value'''
        self._curr_temp = self.temp_sensor.temp
        return self._curr_temp

    def update_room_size(self):
        '''Reads distance sensor and updates room_size variable'''
        self._room_size = self.distance_sensor.distance ** 2
        return self._room_size

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
        self._is_heating = not self._is_heating
        return self._is_heating

    def switch_system(self):
        '''Toggles system between 'Adaptive' and 'Manual' modes and returns value'''
        self._system = 'Adaptive' if self._system == 'Manual' else 'Manual'

    def get_img(self):
        '''function to grab the image from the camera'''
        return self.camera.get_img()

    def get_therm_img(self):
        '''function to grab thermal image from thermal camera'''
        return self.therm_camera.therm_img

    #getters
    @property 
    def is_on(self):
        return self._is_on

    @property
    def degree(self):
        return self._degrees

    @property
    def min_temp(self):
        return self._min_temp

    @property
    def max_temp(self):
        return self._max_temp

    @property
    def curr_temp(self):
        return self._curr_temp

    @property
    def desired_temp(self):
        return self._desired_temp

    @property
    def num_people(self):
        return self._num_people

    @property
    def motion(self):
        return self._motion

    @property
    def room_size(self):
        return self.update_room_size()
    
    @property
    def sound(self):
        return self._sound

    @property
    def mode(self):
        return self._is_heating

    @property
    def fan(self):
        return self._fan
    
    @property
    def system(self):
        return self._system

    #setters
    @min_temp.setter
    def min_temp(self, t):
        self._min_temp = t
        if self._desired_temp < self._min_temp:
            self._desired_temp = self._min_temp

    @max_temp.setter
    def max_temp(self, t):
        self._max_temp = t
        if self._desired_temp > self._max_temp:
            self._desired_temp = self._max_temp

    def algorithm(self):
        '''main algorithm of the thermostat, handles all aspects of thermostat logic'''
        #make sure thermostat is on before running algorithm
        if not self.is_on:
            return

        if self._system == 'Adaptive':
            #TODO: Adaptive functionality
            return
        elif self._system == 'Manual':
            #TODO: Manual functionality
            return
    
# --------------------- End Helper Functions  ---------------------  

# --------------------- Entry Point  ---------------------  

# begin execution of the thermostat program
if __name__ == '__main__':
    thermostat = Thermostat()