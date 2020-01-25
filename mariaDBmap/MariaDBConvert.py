import pandas as pd
import json
import os
import csv
import pprint

with open("database.json", "r") as read_file:
    data = json.load(read_file)
    
headers = ['JSON Datatype','datatype','precision','scale', 'max length']
definitions = []

for row in data['dataTypes']:
    l0 = row['JSONDataType']
    l1 = row['dataType']
    if 'precision' in row:
        l2 = row['precision']
    else:
        l2 = None
    if 'scale' in row:
        l3 = row['scale']
    else:
        l3 = None
    if 'maxLength' in row:
        l4 = row['maxLength']
    else:
        l4 = None 


    
    addrow = [l0, l1, l2, l3, l4]
    definitions.append(addrow)
    
    
    
typelist = definitions.insert(0,headers)
typelist = definitions

import csv

with open("typelist.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(typelist)