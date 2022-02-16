import pandas as pd
import json

with open('template.json','r') as f:
    data = json.loads(f.read())

df_nested_list = pd.json_normalize(data, record_path=['results'])
df_nested_list.to_csv('output.csv')
