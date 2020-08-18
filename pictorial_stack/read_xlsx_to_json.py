 # -*- coding: utf-8 -*-
import pandas as pd
import json
from itertools import groupby 

df = pd.read_excel("Copy of Lịch trình và tổng hợp ca dương tính 18_08 8h55.xlsx", sheet_name="DS Tổng hợp 8h55", usecols=['Triệu chứng khởi phát'], converters = {'Triệu chứng khởi phát':str})
ls = []
df.columns = ['name']
for i in df.name:
    if str(i) !='nan':
        for n in i.lower().split(sep=', '):
            if 'họng' in n or 'rát' in n:
                ls.append('đau họng')
            elif 'sốt' in n or 'mũi' in n or 'cúm' in n:
                ls.append('sốt')
            elif 'mệt' in n or 'mỏi' in n or 'nhức' in n:
                ls.append('mệt mỏi')
            elif 'ngực' in n:
                ls.append('tức ngực')
            elif 'ho' in n:
                ls.append('ho khan')
            else:
                ls.append(n)
res = []
for key, group in groupby(sorted(ls)):
    l = len(list(group))
    if l > 2:
        dic = {}
        dic['name'] = key
        dic['value'] = l
        res.append(dic)
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, ensure_ascii=False)
