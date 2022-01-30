#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from datetime import datetime, timedelta
from subprocess import Popen
import json

chList = []
now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000Z')
later = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S.000Z')

url = f"http://api.pluto.tv/v2/channels"
r = requests.get(url)

data = r.json()

for ch in data:
    name = ch['name']
    print(name)
    chList.append(name)

url = f"http://api.pluto.tv/v2/channels?start={now}&stop={later}"
print(url)
r = requests.get(url)

### to json 
data = r.json() 

def getValues(channel):
    theList = []
    for i in data:
        if i['name'] == channel:
            pr = i['timelines']
            for a in pr:
                title = str(a.get('title'))
                st = a.get('start')
                start = st[11:16]
                desc = a["episode"]["series"].get("description")
                theList.append(f"{start} Uhr: {title}\n{desc}\n")
    return theList
    
with open("/tmp/plutoProgramm.txt", "w") as f:
    for ch in chList:   
        f.write(f"######## {ch.replace('Pluto TV ', '')} ########\n")
        
        f.write('\n'.join(getValues(ch)))
        f.write('\n\n')
    f.close()
    
Popen(["xdg-open", "/tmp/plutoProgramm.txt"])
                
