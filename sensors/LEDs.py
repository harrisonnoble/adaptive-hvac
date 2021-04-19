# LEDs.py
# Written by Harrison Noble

from gpiozero import LED

class LEDs:
    '''Class to handle turning the LEDs on and off'''

# --------------------- Init Function  ---------------------

    def __init__(self):
        self._fan_led = LED(20)
        self._ac_led = LED(21)
        self._heat_led = LED(16)

        self._fan_led.off()
        self._ac_led.off()
        self._heat_led.off()

# --------------------- End Init Function  ---------------------  

# --------------------- Helper Functions  --------------------- 

    def fan_on(self):
        '''Function to turn fan LED on'''
        self._fan_led.on()

    def fan_off(self):
        '''Function to turn fan LED off'''
        self._fan_led.off()

    def ac_on(self):
        '''Function to turn AC LED on'''
        self._ac_led.on()

    def ac_off(self):
        '''Function to turn AC LED on'''
        self._ac_led.off()

    def heat_on(self):
        '''Function to turn heat LED on'''
        self._heat_led.on()

    def heat_off(self):
        '''Function to turn heat LED on'''
        self._heat_led.off()

    @property
    def fan_status(self):
        '''Function to check if fan LED is on (True) or off (False)'''
        return True if self._fan_led.value == 1 else False

    @property
    def ac_status(self):
        '''Function to check if AC LED is on (True) or off (False)'''
        return True if self._ac_led.value == 1 else False

    @property
    def heat_status(self):
        '''Function to check if heat LED is on (True) or off (False)'''
        return True if self._heat_led.value == 1 else False

# --------------------- End Helper Functions  --------------------- 