# AudioSensor.py
# written by Harrison Noble

import RPi.GPIO as GPIO

class AudioSensor:
    '''AudioSensor class to handle the interfacing with the DAOKI sound sensor'''

# --------------------- Init Function  ---------------------  

    def __init__(self):
        self._sound = False

        self._pin = 17

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._pin, GPIO.IN)
        GPIO.add_event_detect(self._pin, GPIO.BOTH, bouncetime=300)
        GPIO.add_event_callback(self._pin, self.audio_callback)

# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  ---------------------  

    def audio_callback(self):
        '''function to run when audio sensor detects or stops detecting sound'''
        if GPIO.input(self._pin):
            self._sound = True
        else:
            self._sound = False

    #getter
    @property
    def sound(self):
        '''property that returns sound boolean, true if sound detected, false if no sound detected'''
        return self._sound

# --------------------- End Helper Functions  ---------------------  