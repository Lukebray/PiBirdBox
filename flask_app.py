from flask import Flask, render_template, jsonify
from datetime import datetime, timedelta
import pandas as pd
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
    print(value)

    tempData = []
    humData = []
    rainData = []
    labels = []

    c.execute("SELECT temp, humidity, rain, datetime FROM data ORDER BY datetime DESC LIMIT 1;")
    currentRow = c.fetchall()
    currentData = list(currentRow)

    currentTemp = currentData[0][0]
    currentHum = currentData[0][1]
    currentRain = currentData[0][2]

    if days == 7 or days == 30:
        c.execute("SELECT temp, humidity, rain, datetime FROM data WHERE datetime >= %s ORDER BY datetime DESC;", (value,))

        rows = c.fetchall()

        df = pd.DataFrame(rows, columns=['temp', 'hum', 'rain', 'date']).set_index('date')

        df_day = df.resample('d').mean().fillna(0)
        print('DF_DAY IS BELOW THIS')
        print(df_day)

        for index, row in df_day.iterrows():

            tempData.insert(0, row['temp'])
            humData.insert(0, row['hum'])
            rainData.insert(0, row['rain'])
            labels.insert(0, str(index.date()))

        tempData.reverse()
        humData.reverse()
        rainData.reverse()
        labels.reverse()

        latestRain = rainData[-1]
        isRaining = True

        if (latestRain == 1):
            isRaining = True
        else:
            isRaining = False

        return jsonify({'payload':json.dumps({'tempData':tempData, 'humData':humData, 'isRaining':isRaining, 'labels':labels, 'currentTemp':currentTemp, 'currentHum':currentHum, 'currentRain':currentRain})})

    elif days == 1:
        c.execute("SELECT temp, humidity, rain, datetime FROM data WHERE datetime >= %s ORDER BY datetime DESC;", (value,))

        rows = c.fetchall()

        df = pd.DataFrame(rows, columns=['temp', 'hum', 'rain', 'date']).set_index('date')
        df_hour = df.resample('H').mean().fillna(0)
        print('DF_HOUR IS BELOW THIS')
        print(df_hour)

        for index, row in df_hour.iterrows():

            tempData.insert(0, row['temp'])
            humData.insert(0, row['hum'])
            rainData.insert(0, row['rain'])
            labels.insert(0, str(index.time()))

        tempData.reverse()
        humData.reverse()
        rainData.reverse()
        labels.reverse()

        latestRain = rainData[-1]
        isRaining = True

        if (latestRain == 1):
            isRaining = True
        else:
            isRaining = False

        return jsonify({'payload':json.dumps({'tempData':tempData, 'humData':humData, 'isRaining':isRaining, 'labels':labels, 'currentTemp':currentTemp, 'currentHum':currentHum, 'currentRain':currentRain})})

    else:
        c.execute("SELECT temp, humidity, rain, datetime FROM data ORDER BY datetime DESC LIMIT 25;")
        currentRows = c.fetchall()

        for r in currentRows:

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

        return jsonify({'payload':json.dumps({'tempData':tempData, 'humData':humData, 'isRaining':isRaining, 'labels':labels, 'currentTemp':currentTemp, 'currentHum':currentHum, 'currentRain':currentRain})})

if __name__ == "__main__":
    app.run()


