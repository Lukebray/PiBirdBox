import pymysql
import sshtunnel

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

with sshtunnel.SSHTunnelForwarder(
    ('ssh.pythonanywhere.com'),
    ssh_username='davidplatt', ssh_password='H@mp5t3Ad',
    remote_bind_address=('davidplatt.mysql.pythonanywhere-services.com', 3306)
) as tunnel:
    connection = pymysql.connect(host='davidplatt.mysql.pythonanywhere-services.com',
                       user='davidplatt',
                       password='tinwhistle',
                       db='davidplatt$default',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor                           
                                 )


try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO 'users' ('email', 'password') VALUES (%s, %s)"
        cursor.execute(sql('lukebray@hotmail.co.uk', 'mypassword'))
        connection.commit()

finally:
    connection.close()