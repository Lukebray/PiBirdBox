import pandas as pd
import datetime

data = [(21, 55, datetime.datetime(2019, 4, 29, 9, 57, 53)), 
(22, 55, datetime.datetime(2019, 4, 29, 9, 56, 52)), 
(26, 47, datetime.datetime(2019, 4, 29, 9, 55, 49)), 
(22, 54, datetime.datetime(2019, 4, 30, 9, 54, 49)), 
(20, 54, datetime.datetime(2019, 4, 30, 9, 53, 49)), 
(19, 65, datetime.datetime(2019, 5, 1, 9, 52, 48)), 
(18, 53, datetime.datetime(2019, 5, 1, 9, 51, 47)), 
(21, 58, datetime.datetime(2019, 5, 1, 9, 50, 46))]

df = pd.DataFrame(data, columns=['temp', 'hum', 'date']).set_index('date')
df_day = df.resample('d').mean()

print(df_day)

tempData = []
humData = []
labels = []

for index, row in df_day.iterrows():
    tempData.insert(0, row['temp'])
    humData.insert(0, row['hum'])
    labels.insert(0, index,)

tempData.reverse()
humData.reverse()
labels.reverse()
print(tempData)
print(humData)
print(labels)
print(labels[0])
