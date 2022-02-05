from os import sep
import requests
from bs4 import BeautifulSoup
from requests.api import head

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

url = 'https://comic.naver.com/webtoon/list?titleId=675554'
res = requests.get(url, headers= headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

title = soup.select('td.title a')
stars = soup.select('.rating_type strong')
for tl, star in zip(title, stars):
    print(tl.get_text(),"https://comic.naver.com" + tl['href'], star.get_text())
