# AudioSensor.py
# written by Harrison Noble

import RPi.GPIO as GPIO
import time

class AudioSensor:
    '''AudioSensor class to handle the interfacing with the DAOKI sound sensor'''

# --------------------- Init Function  ---------------------  

    def __init__(self):
        self._sound = False
        self._pin = 27
        self._sound_func = None

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._pin, GPIO.IN)
        GPIO.add_event_detect(self._pin, GPIO.BOTH, callback=self._audio_callback, bouncetime=1000)
        #GPIO.add_event_callback(self._pin, self.audio_callback, bouncetime=1000)

# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  --------------------- 

    def _audio_callback(self, pin):
        '''function to run when audio sensor detects or stops detecting sound'''
        if GPIO.input(pin):
            self._sound = True
            #print('sound')
            if self._sound_func:
                self._sound_func()
            time.sleep(1)
        else:
            self._sound = False
            #print('no sound')
            if self._sound_func:
                self._sound_func()

    def set_sound_func(self, func):
        '''Function used to add an additional function call when audio_callback function is run'''
        if func:
            self._sound_func = func

    #getter
    @property
    def sound(self):
        '''property that returns sound boolean, true if sound detected, false if no sound detected'''
        return self._sound

# --------------------- End Helper Functions  ---------------------  