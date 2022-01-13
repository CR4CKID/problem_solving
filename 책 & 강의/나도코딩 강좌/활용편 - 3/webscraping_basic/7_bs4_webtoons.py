import requests
from bs4 import BeautifulSoup
from requests.api import head

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url, headers= headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가져오기
daily = soup.select('a.title') # class 속성이 title인 모든 a element 반환
for web in daily:
    print(web.get_text(), end=", ")