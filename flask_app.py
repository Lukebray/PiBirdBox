from flask import Flask, render_template, jsonify
import mysql.connector
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/get_data')
def get_data():
    conn = mysql.connector.connect(
    host='davidplatt.mysql.pythonanywhere-services.com',
    user='davidplatt',
    passwd='tinwhistle',
    db='davidplatt$WeatherData')

    c = conn.cursor()

    c.execute("SELECT temp, humidity, rain, datetime FROM data ORDER BY datetime DESC LIMIT 20;")

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

        datetime = str(data[3])
        labels.insert(0, datetime)

    latestRain = rainData[-1]
    isRaining = True

    if (latestRain == 1):
        isRaining = True
    else:
        isRaining = False

    return jsonify({'payload':json.dumps({'tempData':tempData, 'humData':humData, 'isRaining':isRaining, 'labels':labels})})

if __name__ == "__main__":
    app.run()


