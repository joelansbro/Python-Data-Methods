import pandas as pd
import requests
import json
import time

def fetch(url: str) -> list:
    res = requests.get(url)
    return json.loads(res.content)


def process(person: list) -> pd.DataFrame:
    pass

# load data using Python JSON module
if __name__ == '__main__':
    loop = True
    while(loop):
        posts = fetch(url="https://randomuser.me/api/")
        print(posts)
        time.sleep(5)
