import json
import requests
import pandas as pd
from datetime import datetime
import time


# fetch json
def fetch(url: str) -> list:
    res = requests.get(url)
    return json.loads(res.content)

# process straight to dataframe
def process(posts: list) -> pd.DataFrame:
    processed = []
    for post in posts:
        processed.append({
            'ID': post['id'],
            'UserID': post['userId'],
            'Title': post['title']
        })
    return pd.DataFrame(processed)

if __name__ == '__main__':
    loop = True
    while(loop):
        posts = fetch(url="https://jsonplaceholder.typicode.com/posts")
        posts = process(posts=posts)
        print(posts)
        time.sleep(5)
