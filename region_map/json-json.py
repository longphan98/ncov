import requests
from pandas.io.json import json_normalize
import pandas as pd
import json

url = "map.json"
df = pd.read_json(url,encoding='utf-8')
dat = pd.read_csv("data.csv", header=None, encoding='utf-8')
dic = {}
for row in df['features']:
    if row['properties']['name'] in dat[0].to_list():
        dic[row['properties']['id']] = int(dat[dat[0]==row['properties']['name']][1])
with open('dat.json', 'w', encoding='utf-8') as f:
        json.dump([{'id': k, 'value': v} for k,v in dic.items()], f, ensure_ascii=False, indent=4)