import RPi.GPIO as GPIO
import dht11
import rainSensor
import time
import datetime
import mysql.connector
from mysql.connector import Error
import sshtunnel

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

temphum = dht11.DHT11(pin = 21)
GPIO.cleanup()

rain = rainSensor.RainSensor(pin = 17)
GPIO.cleanup()

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

def weatherData():
    while True:
            resultDHT = temphum.read()
            resultRain = rain.read()
            if resultDHT.is_valid():
                print("Last Valid Input: " + str(datetime.datetime.now()))
                print ("Temperature: %d C" % resultDHT.temperature)
                print ("Humidity: %d %%" % resultDHT.humidity)
                print ("Raining?: %d" % resultRain)
                query = "INSERT INTO data (temp, humidity, rain, datetime) VALUES (%s, %s, %s, %s)"
                args = (resultDHT.temperature, resultDHT.humidity, resultRain, datetime.datetime.now())

                cursor.execute(query, args)
                connection.commit()
                time.sleep(60)
            else:
                print("Error ", resultDHT.error_code)


 
if __name__ == '__main__':
    with sshtunnel.SSHTunnelForwarder(
    ('ssh.pythonanywhere.com'),
    ssh_username='davidplatt', ssh_password='H@mp5t3Ad',
    remote_bind_address=('davidplatt.mysql.pythonanywhere-services.com', 3306)
) as tunnel:
        connection = mysql.connector.connect(
        user='davidplatt', password='tinwhistle',
        host='127.0.0.1', port=tunnel.local_bind_port,
        database='davidplatt$WeatherData',       
    )
        db_info = connection.get_server_info()
        if connection.is_connected():
            cursor = connection.cursor()
            print('Connected to MySQL DB...version on ', db_info)
            weatherData()
        else:
            print('Failed to connect to database.')
    
        connection.close()