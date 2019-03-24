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

    c.execute("SELECT temp, humidity, datetime FROM data;")

    rows = c.fetchall()

    tempData = []
    humData = []
    labels = []
    for r in rows:
        data = list(r)
        temp = data[0]
        tempData.append(temp)

        hum = data[1]
        humData.append(hum)

        datetime = str(data[2])
        labels.append(datetime)

    return jsonify({'payload':json.dumps({'tempData':tempData, 'humData':humData, 'labels':labels})})

if __name__ == "__main__":
    app.run()


