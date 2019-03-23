
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    connection = mysql.connector.connect(
        user='davidplatt', password='tinwhistle',
        host='127.0.0.1', port=tunnel.local_bind_port,
        database='davidplatt$WeatherData',       
    )
    if connection.is_connected():
        return 'Hello there!' 

