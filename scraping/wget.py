import wget

with open('imagelist.txt','r') as f:
    url_list = [line.strip() for line in f]

for url in url_list:
    filename = wget.download(url)