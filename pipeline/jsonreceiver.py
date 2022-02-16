import pandas as pd
import requests
import json
import time
from datetime import datetime

def fetch(url: str) -> list:
    res = requests.get(url)
    return json.loads(res.content)

def dump(person: dict):
    json_string = json.dumps(person, skipkeys = True)
    curr_timestamp = int(datetime.timestamp(datetime.now())) 
    f = open(f'./_{curr_timestamp}.json', "x")
    f.write(json_string)

# load data using Python JSON module
if __name__ == '__main__':
    loop = True
    while(loop):
        person = fetch(url="https://randomuser.me/api/")
        dump(person)
        time.sleep(5)
