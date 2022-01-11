from os import sep
import requests
from bs4 import BeautifulSoup
import re, sys

print('네이버 주요 뉴스들을 추출하고 있습니다. \n\
20초만 기다려 주세요.\n')

f = open('네이버 뉴스 타이틀.txt', 'w', encoding='utf-8')


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWe\
    bKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.277 Whale/2.9.118.38 Saf\
        ari/537.36'}

i = 1
loading = 0
# 각 뉴스페이지에서 타이틀과 시간 추출
def title_time(income_url):
    global i, loading
    url = income_url
    req = requests.get(url, headers=headers)
    bs = BeautifulSoup(req.content.decode('euc-kr', 'replace'), 'html.parser')
    try:
        title = bs.select_one('h3#articleTitle').text
        print('{0}. {1}'.format(i, title),file=f, end= '\n\n')
        sys.stdout.write("\r로딩중: {}%".format(round(loading, 2)))
        loading += 1.4
        # print('{0}. {1} \n {2}'.format(i, title, url), end= '\n\n')
        i += 1
    except AttributeError:
        return 0

# 네이버 뉴스 메인에서 타이틀 뉴스 url 추출
url = 'https://news.naver.com'
req = requests.get(url, headers=headers)
bs = BeautifulSoup(req.content, 'html.parser')
links = set()

for link in bs.findAll('a', href = re.compile('^(/main/ranking/read)')):
    if link.attrs['href'] is not None:
        if link.attrs['href'] not in links:
            links.add(link.attrs['href'])


for link in links:
    title_time(url + link)

f.close()