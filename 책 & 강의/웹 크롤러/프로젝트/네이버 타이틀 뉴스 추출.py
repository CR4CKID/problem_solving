import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWe\
    bKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.277 Whale/2.9.118.38 Saf\
        ari/537.36'}

# 각 뉴스페이지에서 타이틀과 시간 추출
def title_time(income_url):
    url = income_url
    req = requests.get(url, headers=headers)
    bs = BeautifulSoup(req.content.decode('euc-kr', 'replace'), 'html.parser')
    title = bs.select_one('h3#articleTitle').text
    print(str(i+1)+".", title)

# 네이버 뉴스 메인에서 타이틀 뉴스 url 추출
url = 'https://news.naver.com'
req = requests.get(url, headers=headers)
bs = BeautifulSoup(req.content, 'html.parser')
for i, link in enumerate(bs.select('div.hdline_article_tit a')):
    title_time(url + link.attrs['href'])

