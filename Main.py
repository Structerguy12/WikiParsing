import requests
from bs4 import BeautifulSoup

# http 
# 200 - connect is ok
# 404 - error

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

response = requests.get(url)

if response.status_code == 200:
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    result = soup.select("#mw-content-text p")
    with open("banana.txt", 'r', encoding='utf-8') as file:
        TextFile = file.read()
        print(TextFile)

else:
    print('error')
