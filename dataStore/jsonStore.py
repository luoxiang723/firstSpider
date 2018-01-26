# encoding=utf-8

import requests
from bs4 import BeautifulSoup
import json
import chardet

user_agent = 'Mozilla/4.0 (compatibel; MSIE 5.5; Windows NT)'
headers = {"User_agent": user_agent}
response = requests.get("http://seputu.com/", headers=headers)

soup = BeautifulSoup(response.text, 'html.parser', from_encoding='utf-8')
content = []
for mulu in soup.find_all(class_='mulu'):
    h2 = mulu.find('h2')
    if h2 != None:
        mulu_title = h2.string
        list = []
        for a in mulu.find(class_='box').find_all('a'):
            href = a.get('href')
            box_title = a.get('title')
            list.append({'href': href, 'box_title': box_title})
        content.append({'title': mulu_title, 'content': list})

with open('jsonStore.txt', 'w') as jsonWriter:
    json.dump(content,fp=jsonWriter)

# with open('jsonStore.txt','rb') as jsonReader:
#     jsonStr = json.load(jsonReader,)
# print jsonStr
