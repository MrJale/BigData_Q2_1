#!/usr/bin/python
# --*-- coding:utf-8 --*--
import csv
import sys

# with open(sys.stdin, "r", encoding = "utf-8") as f:
#     reader = csv.reader(f)
#     headers = next(f)
#     rows = [row for row in reader]

reader = csv.reader(sys.stdin)
reader.__next__()
    
dic = {}

made, missed = 0, 0
for row in reader:
    pair = (row[19],row[14])
    if pair not in dic.keys():
        dic[pair]=[0,0]
    
    if row[13] == 'made':
        dic[pair][0] += 1
    else:
        dic[pair][1] += 1
        
for k,v in dic.items():
#     print(k[0],"@",k[1],"@",v[0],"@",v[1])
    print '%s@%s@%s@%s' % (k[0],k[1],v[0],v[1])
