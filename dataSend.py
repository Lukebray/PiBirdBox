import RPi.GPIO as GPIO
import dht11
import rainSensor.py
import time
import datetime
import mysql.connector
from mysql.connector import Error
import sshtunnel

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

temphum = dht11.DHT11(pin = 4)
rain = rainSensor.RainSensor(pin = 18)


sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

def weatherData():
    while True:
            result = temphum.read()
            if result.is_valid():
                print("Last Valid Input: " + str(datetime.datetime.now()))
                print ("Temperature: %d C" % result.temperature)
                print ("Humidity: %d %%" % result.humidity)
                query = "INSERT INTO data (temp, humidity, datetime) VALUES (%s, %s, %s)"
                args = (result.temperature, result.humidity, str(datetime.datetime.now()))

                cursor.execute(query, args)
                connection.commit()
                time.sleep(5)
            else:
                print("Error ", result.error_code)


 
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
            dataHandler()
        else:
            print('Failed to connect to database.')
    
        connection.close()