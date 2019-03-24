#from flask import Flask, render_template
import mysql.connector

conn = mysql.connector.connect(
    host='davidplatt.mysql.pythonanywhere-services.com',
    user='davidplatt',
    passwd='tinwhistle',
    db='davidplatt$WeatherData'
    )

c = conn.cursor()

c.execute("SELECT temp FROM data;")

rows = c.fetchall()

tempData = []
labels = []
for r in rows:
    s = list(r)
    x = s[0]
    tempData.append(x)

for i in range(0, len(rows)):
    labels.append(i)


print(tempData)
print(labels)

    #return render_template("main.html", tempData=tempData, labels=labels)


