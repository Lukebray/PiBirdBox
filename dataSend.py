    import RPi.GPIO as GPIO
    import dht11
    import time
    import datetime
    import mysql.connector
    from mysql.connector import Error
    import sshtunnel

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

    instance = dht11.DHT11(pin = 4)

    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

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
            while True:
                result = instance.read()
                if result.is_valid():
                    query = "INSERT INTO data (temp, humidity, datetime) VALUES (%s, %s, %s)"
                    args = (result.temperature, result.humidity, str(datetime.datetime.now()))

                    cursor.execute(query, args)
                    connection.commit()
                    cursor.close()
                else:
                    print("Error %d", %result.error_code)

        else:
            print('Failed to connect to database.')
    
        connection.close()


'''
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

'''
        