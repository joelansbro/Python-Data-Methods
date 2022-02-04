import requests

url = "http://mockbin.com/request"

querystring = {"foo":["bar","baz"]}

payload = "{\"foo\": \"bar\"}"
headers = {
    'cookie': "foo=bar; bar=baz",
    'x-pretty-print': "2"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)