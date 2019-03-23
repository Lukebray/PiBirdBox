
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello_world():
    connection = mysql.connector.connect(
    host='davidplatt.mysql.pythonanywhere-services.com',
    user='davidplatt',
    passwd='tinwhistle',
    db='davidplatt$WeatherData')

    if connection.is_connected():
        return 'Hello there!'
    else:
        return 'No hello for you'

