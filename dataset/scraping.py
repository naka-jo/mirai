import copy
import time
import requests
from bs4 import BeautifulSoup


url = 'http://www.sainet.or.jp/~eshibuya/'
res = requests.get(url)
session = requests.Session()

soup = BeautifulSoup(res.content, 'html.parser')

soup_a = soup.find_all('a')
urls_original = []
urls_modern = []
number_list = []
for a in soup_a:
    text = a.get_text()
    if text == '本文':
        urls_original.append(url+a.get('href'))
        number_list.append(a.get('href')[4:6])
    elif text == '現代語訳':
        urls_modern.append(url+a.get('href'))

url_title = 'https://ja.wikipedia.org/wiki/%E6%BA%90%E6%B0%8F%E7%89%A9%E8%AA%9E%E3%81%AE%E5%B7%BB%E5%BA%8F'
res = session.get(url_title)

soup = BeautifulSoup(res.text, 'html.parser')

soup_li = soup.find('div', class_='div-col columns column-width').find_all('li')
title_list = []
for li in soup_li:
    text = li.get_text()
    title_list.append(text)
    
title_2 = ['紫式部日記', '紫式部集']
title_list = title_2 + title_list
title_list_modern = copy.copy(title_list)
title_list_modern = [title+'modern' for title in title_list_modern]
count = 10

def scraping_body(file, urls, titles):
    count = 10
    for url, title in zip(urls, titles):
        try:      
            res = requests.get(url)
            soup = BeautifulSoup(res.content, 'html.parser')
            soup_body = soup.find('body')
            with open(f'./{file}/{count}_{title}.txt', 'w') as f:
                f.write(str(soup_body))
        except RecursionError:
            pass
        count += 1
        time.sleep(0.1)

scraping_body('data_original', urls_original, title_list)
scraping_body('data_modern', urls_modern, title_list_modern)