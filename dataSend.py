import RPi.GPIO as GPIO
import dht11
import time
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin = 4)

while True:
    result = instance.read()

    if result.is_valid():
        print("Last Valid Input: " + str(datetime.datetime.now()))
        print ("Temperature: %d C" % result.temperature)
        print ("Humidity: %d %%" % result.humidity)
    else:
        print ("Error %d" %result.error_code)
    time.sleep(3)