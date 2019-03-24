from flask import Flask, render_template
import json
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello_world():

    conn = mysql.connector.connect(
    host='davidplatt.mysql.pythonanywhere-services.com',
    user='davidplatt',
    passwd='tinwhistle',
    db='davidplatt$WeatherData')

    c = conn.cursor()

    c.execute("SELECT temp FROM data WHERE id=1;")

    rows = c.fetchall()
    tempData = []
    for r in rows:
        tempData.append(r)

    return render_template("main.html", tempData=json.dumps(tempData))

if __name__ == "__main__":
    app.run()

