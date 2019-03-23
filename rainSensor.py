import time
import RPi.GPIO as GPIO

class RainSensor():
    'Rain sensor reader class'    
    __pin = 0

    #each instance has a self and a gpio pin
    def __init__(self, pin):
        self.__pin = pin
    
    def read(self):
        GPIO.setup(self.__pin, GPIO.IN)
        state = GPIO.input(self.__pin)
        
        if (state == 0):
            return 1
        else:
            return 0
        