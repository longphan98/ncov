import pandas as pd
import numpy as np
import datetime as dt
import json

df = pd.read_excel("list.xlsx", sheet_name = "DS tổng hợp (17-8 11h58)", usecols = ['Nơi BC ca bệnh','Ngày khởi phát'], converters = {'Ngày khởi phát':pd.to_datetime,'Nơi BC ca bệnh':str})
df.columns = ['place','time']
df['time'] = pd.to_datetime(df.time).dt.date
df = df.sort_values(by=['time','place']).groupby('time')['place'].value_counts().unstack().fillna(0)
ls = []
res = []
dic = {}
for col in df.columns:
    ls.append(col)
for index,row in df.iterrows():
    dic['date'] = str(row.name)
    for n in range(len(ls)):
        dic[ls[n]] = int(row[n])
    res.append(dic)
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, ensure_ascii=False, indent = 1)