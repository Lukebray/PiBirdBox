import mysql.connector
from mysql.connector import Error
import sshtunnel
import time

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
        database='davidplatt$default',       
    )
    db_info = connection.get_server_info()
    if connection.is_connected():    
        print('Connected to MySQL DB...version on ', db_info)
    else:
        print('Failed to connect.')

    
    connection.close()