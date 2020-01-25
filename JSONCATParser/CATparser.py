#CODE SETUP
import pandas as pd
import json
import os
import csv
import pprint

with open("database.json", "r") as read_file:
    data = json.load(read_file)
    

#PARSER CODE
#takes cat name
eightlist = []
CATROW = []
n = 0

for row in data['eventDefinitions']: # iterates over CATs
    #print(row['eventName'])
    l1 = row['eventName']
    n += 1
    for var in data['eventDefinitions'][n-1]['fields']: #for each gat, iterates over fields
        #print(var['name'])
        l2 = var['name']
        l3 = var['position']
        l4 = var['required']
        l5 = var['dataType']
        l6 = var['JSONDataType']
        if l5 == 'Choice':
            l7 = data['choices'][l2]
        else:
            l7 = None
        if "arrayElements" in var:
            l8 = 'Array Elements exist'
        else:
            l8 = None

        catrow = [l1, l2, l3, l4, l5, l6, l7, l8]
        eightlist.append(catrow)
        
#ADDS HEADERS TO DATA

headers = ['Event Name', 'Data Element Name', 'Position', 'Required', 'Data Type', 'JSON Data Type', 'Choices', 'Array Elements']

CAT_list = eightlist.insert(0,headers)
CAT_list = eightlist



## SAVES OUTPUT AS CSV

import csv

with open("output.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(CAT_list)
