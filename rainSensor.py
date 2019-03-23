import time
import RPi
 
class RainSensor:
    'Rain sensor reader class'
    
    __pin = 0

    def __init__(self, pin):
        self.__pin = pin
    
    def read(self):
        GPIO.setup(self.__pin, GPIO.IN)
        state = GPIO.input(self.__pin)
        
        if (state == 0):
            return True
        else:
            return False
        