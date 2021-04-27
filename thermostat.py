#!/usr/bin/python3

# thermostat.py
# written by Harrison Noble
#THIS IS THE MAIN ENTRYPOINT FOR THE PROGRAM

from gui import Gui
from sensors import *
import configparser
import os
import time
import sys

class Thermostat:
    '''Thermostat class creates UI and all sensors. This is the main entry point for program. To begin program 
    run 'python3 thermostat.py'. After initializing all needed components, program will begin the execution
    of the main loop which handles all UI and thermostat logic'''

# --------------------- Init Function  ---------------------  

    def __init__(self):
        #first read in the config file
        self._cfg = self._read_config()

        #Initialize all sensors & cameras
        self._audio_sensor = AudioSensor()
        self._motion_sensor = MotionSensor()
        self._temp_sensor = TempSensor(self._cfg.get('thermostat', 'degree'))
        self._therm_camera = ThermalCamera()
        self._distance_sensor = DistanceSensor()
        self._camera = Camera()
        self._leds = LEDs()

        #initialize all needed variables for thermostat execution
        self._is_on = self._cfg.getboolean('thermostat', 'on', fallback=str(True))
        self._degrees = self._temp_sensor.mode
        self._min_temp = self._cfg.getint('thermostat', 'min_temp')
        self._max_temp = self._cfg.getint('thermostat', 'max_temp')
        self._curr_temp = self._temp_sensor.temp
        self._desired_temp = self._cfg.getint('thermostat', 'desired_temp')
        self._num_people = 0
        self._motion = self._motion_sensor.motion
        self._room_size = self._distance_sensor.distance ** 2
        self._sound = self._audio_sensor.sound
        self._is_heating = self._cfg.getboolean('thermostat', 'heat', fallback=str(True))
        self._fan = self._cfg.getboolean('thermostat', 'fan', fallback=str(False))
        self._system = self._cfg.get('thermostat', 'system')
        self._reaching_temp = True

        #bind motion/no motion detection functions
        self._motion_sensor.set_motion_func(self._motion_func)
        self._motion_sensor.set_no_motion_func(self._no_motion_func)

        #bind sound detection to updating sound variable
        self._audio_sensor.set_sound_func(self._sound_func)

        #create GUI and start
        self._app = Gui(self)
        self._app.title('Thermostat')
        self._app.mainloop()

# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  ---------------------  

    def _motion_func(self):
        '''function that runs when motion is detected, updates number of people and sets motion value to true'''
        if self._motion_sensor:
            self._motion = self._motion_sensor.motion
            self._update_num_people()

    def _no_motion_func(self):
        '''function to run when motion is not detected, updates motion value to false'''
        if self._motion_sensor:
            self._motion = self._motion_sensor.motion

    def _sound_func(self):
        '''function to run when audio is detectued, updates sound variable'''
        if self._audio_sensor:
            self._sound = self._audio_sensor.sound
    
    def _update_num_people(self):
        '''function to detect number of people and update value'''
        if self._camera:
            self._num_people = self._camera.num_people

    def _update_curr_temp(self):
        '''Reads temperature sensor and updates curr_temp variable'''
        if self._temp_sensor:
            self._curr_temp = self._temp_sensor.temp

    def _update_room_size(self):
        '''Reads distance sensor and updates room_size variable'''
        if self._distance_sensor:
            self._room_size = self._distance_sensor.distance ** 2

    def _toggle_temps(self):
        '''function to update min temp, max temp, and desired temp based on degree'''
        if self._degrees == 'C': #F to C
            self._min_temp = round((self._min_temp - 32) * (5/9))
            self._max_temp = round((self._max_temp - 32) * (5/9))
            self._desired_temp = round((self._desired_temp - 32) * (5/9))
        else: #C to F
            self._min_temp = round((self._min_temp * 1.8) + 32)
            self._max_temp = round((self._max_temp * 1.8) + 32)
            self._desired_temp = round((self._desired_temp * 1.8) + 32)

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
        
        return cfg

    def _write_config(self):
        '''Function to update and write configurable variables to the config.ini file'''
        self._cfg.set('thermostat', 'on', str(self._is_on))
        self._cfg.set('thermostat', 'degree', str(self._degrees))
        self._cfg.set('thermostat', 'min_temp', str(self._min_temp))
        self._cfg.set('thermostat', 'max_temp', str(self._max_temp))
        self._cfg.set('thermostat', 'desired_temp', str(self._desired_temp))
        self._cfg.set('thermostat', 'heat', str(self._is_heating))
        self._cfg.set('thermostat', 'fan', str(self._fan))
        self._cfg.set('thermostat', 'system', str(self._system))

        with open('config.cfg', 'w') as configfile:
            configfile.write('; DO NOT EDIT\n')
            self._cfg.write(configfile)
    
    def save(self):
        '''Function to save config and gracefully close'''
        #close window and write config
        self._app.destroy()
        self._write_config()

        #delete all sensor/camera/led objects
        del self._audio_sensor
        del self._motion_sensor
        del self._temp_sensor
        del self._therm_camera
        del self._distance_sensor
        del self._camera
        self._leds.all_off()
        del self._leds

    def reboot(self):
        '''Function to reboot the thermostat'''
        print('Saving & Rebooting...')
        self.save()
        time.sleep(1.5)
        os.execv(sys.executable, ['python3'] + sys.argv)

    def toggle_on(self):
        '''function to toggle thermostat power (returns true if on, false if off)'''
        self._is_on = not self._is_on
        return self._is_on

    def toggle_degree(self):
        '''function to toggle between C and F'''
        self._degrees = self._temp_sensor.toggle_mode()
        self._update_curr_temp()
        self._toggle_temps()
        return self._degrees

    def toggle_mode(self):
        '''Toggles thermostat between 'Heat' and 'Cool' modes and returns value'''
        self._is_heating = not self._is_heating
        return self._is_heating

    def toggle_fan(self):
        '''function to toggle fan on and off, returns true if fan is on, false if fan is off'''
        self._fan = not self._fan
        return self._fan

    def toggle_system(self):
        '''function to switch between adaptive and manual mode, returns the current mode after toggling'''
        self._system = 'Adaptive' if self._system == 'Manual' else 'Manual'
        return self._system

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

    def get_img(self):
        '''function to grab the image from the camera'''
        return self._camera.img

    def get_therm_img(self):
        '''function to grab thermal image from thermal camera'''
        return self._therm_camera.therm_img

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
        return self._room_size
    
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
        #update sensors
        self._update_room_size()
        self._update_curr_temp()

        #make sure thermostat is on before running algorithm
        if not self.is_on:
            self._leds.all_off()
            return

        if self._system == 'Adaptive':
            #calculate alpha value
            alpha = None
            if self._num_people != 0:
                alpha = float(self._room_size) / float(2.5 * self._num_people)

            #run logic based on alpha value
            if alpha == None:
                pass
            elif alpha < 1:
                pass
            elif alpha >= 1:
                pass

            #if thermostat reached the desired temp (+/- small error) turn off HVAC
            if self._reaching_temp and self._curr_temp >= self._desired_temp - 0.2 and self._curr_temp <= self._desired_temp + 0.2:
                self._reaching_temp = False
                self._leds.all_off()
                return

            #if the current temp is still in temperature buffer zone after reaching desired temp, keep HVAC off
            if not self._reaching_temp and self._curr_temp >= self._desired_temp - 0.5 and self._curr_temp <= self._desired_temp + 0.5:
                self._leds.all_off()
                return

            #if curr temp is less than buffer zone and therm is not reaching desired temp
            if not self._reaching_temp and self._curr_temp < self._desired_temp - 0.5:
                self._is_heating = True
                self._fan = False
                self._reaching_temp = True
            #if curr temp is greater than buffer zone and therm is not reaching desired temp
            elif not self._reaching_temp and self._curr_temp > self._desired_temp + 0.5:
                self._is_heating = False
                self._fan = True
                self._reaching_temp = True
            
            #switch to cooling mode if temp is too high
            if self._reaching_temp and self._curr_temp > self._desired_temp + 0.5 and self._is_heating:
                self._is_heating = False
                self._fan = True
            #switch to heating mode if temp is too low
            if self._reaching_temp and self._curr_temp < self._desired_temp - 0.5 and not self._is_heating:
                self._is_heating = True
                self._fan = False

            #toggle LEDs based on above logic
            if self._is_heating:
                self._leds.ac_off()
                self._leds.heat_on()
            else:
                self._leds.heat_off()
                self._leds.ac_on()
            
            if self._fan:
                self._leds.fan_on()
            else:
                self._leds.fan_off()

        elif self._system == 'Manual':
            #if thermostat reached the desired temp (+/- small error) turn off HVAC
            if self._reaching_temp and self._curr_temp >= self._desired_temp - 0.2 and self._curr_temp <= self._desired_temp + 0.2:
                self._reaching_temp = False
                self._leds.all_off()
                return

            #if the current temp is still in temperature buffer zone after reaching desired temp, keep HVAC off
            if not self._reaching_temp and self._curr_temp >= self._desired_temp - 0.5 and self._curr_temp <= self._desired_temp + 0.5:
                self._leds.all_off()
                return

            #the below logic runs if outside temp buffer 
            if self._is_heating:
                self._leds.ac_off()
            else:
                self._leds.heat_off()

            if not self._fan:
                self._leds.fan_off()

            #current temp is greater than the desired temp and therm is in cooling mode
            if self._curr_temp > self._desired_temp and not self._is_heating:
                self._reaching_temp = True
                self._leds.heat_off()
                self._leds.ac_on()
                if self._fan:
                    self._leds.fan_on()

            #current temp is greater than the desired temp and therm is in heating mode
            if self._curr_temp > self._desired_temp and self._is_heating:
                self._leds.heat_off()
                self._leds.fan_off()
                
            #current temp is less than the desired temp and therm is in heating mode
            if self._curr_temp < self._desired_temp and self._is_heating:
                self._reaching_temp = True
                self._leds.ac_off()
                self._leds.heat_on()
                
            #current temp is less than the desired temp and therm is in cooling mode
            if self._curr_temp < self._desired_temp and not self._is_heating:
                self._leds.ac_off()
                if self._fan:
                    self._leds.fan_off()
    
# --------------------- End Helper Functions  ---------------------  

# --------------------- Entry Point  ---------------------  

# begin execution of the thermostat program
if __name__ == '__main__':
    thermostat = Thermostat()
    del thermostat