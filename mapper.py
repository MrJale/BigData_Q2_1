#!/usr/bin/python
# --*-- coding:utf-8 --*--
import csv
import sys

with open(sys.stdin, "r", encoding = "utf-8") as f:
    reader = csv.reader(f)
    headers = next(f)
    rows = [row for row in reader]
    
dic = {}

made, missed = 0, 0
for row in rows:
    pair = (row[19],row[14])
    if pair not in dic.keys():
        dic[pair]=[0,0]
    
    if row[13] == 'made':
        dic[pair][0] += 1
    else:
        dic[pair][1] += 1
        
for k,v in dic.items():
    print(f'{k[0]:20},{k[1]:20},{v[0]:1},{v[1]:1}')