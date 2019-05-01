from flask import Flask, render_template, jsonify
from datetime import datetime, timedelta
import mysql.connector
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/get_data/<days>')
def get_data(days):
    conn = mysql.connector.connect(
    host='davidplatt.mysql.pythonanywhere-services.com',
    user='davidplatt',
    passwd='tinwhistle',
    db='davidplatt$WeatherData')

    c = conn.cursor()

    days = int(days)

    rows = None

    value = datetime.now() - timedelta(days)

    c.execute("SELECT temp, humidity, rain, datetime FROM data WHERE datetime >= '%s' ORDER BY datetime DESC;" % (value))

    rows = c.fetchall()

    tempData = []
    humData = []
    rainData = []
    labels = []
    for r in rows:
        data = list(r)
        temp = data[0]
        tempData.insert(0, temp)

        hum = data[1]
        humData.insert(0, hum)

        rain = data[2]
        rainData.insert(0, rain)

        datetimeval = str(data[3])
        labels.insert(0, datetimeval)

    latestRain = rainData[-1]
    isRaining = True

    if (latestRain == 1):
        isRaining = True
    else:
        isRaining = False

    return jsonify({'payload':json.dumps({'tempData':tempData, 'humData':humData, 'isRaining':isRaining, 'labels':labels})})


if __name__ == "__main__":
    app.run()


