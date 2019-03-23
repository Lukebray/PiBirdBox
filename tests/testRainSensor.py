import time
import RPi.GPIO as GPIO
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

GPIO.setup(17, GPIO.IN)

def sensorTest():
    while True:
        state = GPIO.input(17)
        if (state == 0):
            print("True")
            return True
        else:
            print("False")
            return False     
        time.sleep(1)
        
if __name__ == "__main__":
    while True:
        sensorTest()       
        time.sleep(5)

        