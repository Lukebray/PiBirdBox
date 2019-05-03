import RPi.GPIO as GPIO
import dht11
import rainSensor
import time
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

temphum = dht11.DHT11(pin = 21)
GPIO.cleanup()

rain = rainSensor.RainSensor(pin = 17)
GPIO.cleanup()

def sensorTest():
    while True:
            resultDHT = temphum.read()
            resultRain = rain.read()
            if resultDHT.is_valid():
                print("Last Valid Input: " + str(datetime.datetime.now()))
                print ("Temperature: %d C" % resultDHT.temperature)
                print ("Humidity: %d %%" % resultDHT.humidity)
                print ("Raining?: %d" % resultRain)

            else:
                print("Error ", resultDHT.error_code)
            
            time.sleep(5)
                
if __name__ == "__main__":
    sensorTest()
                