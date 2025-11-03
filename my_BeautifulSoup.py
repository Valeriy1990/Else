
from bs4 import BeautifulSoup
import requests

url = ('https://2051.vision/category/ii/')
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')
top = soup.find_all('div', class_="td-module-meta-info")
filtered = []


for data in top:
    if data.h3 is not None:
        filtered.append(data.h3.string)

for i, k in enumerate(filtered):
    print(i+1, k)
