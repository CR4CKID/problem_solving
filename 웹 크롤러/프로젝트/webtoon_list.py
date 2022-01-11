import requests
from bs4 import BeautifulSoup
import sys



headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

f= open('웹툰 리스트', 'w', encoding='utf-8')

def title_list(url):
    res = requests.get(url, headers= headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    title = soup.select('td.title a')
    for tl in title:
        print(tl.get_text(),"https://comic.naver.com" + tl['href'], file= f)

def each_one(url):
    url = url + '&page=1000'
    res = requests.get(url, headers=headers)
    bs = BeautifulSoup(res.text, 'lxml')

    title = bs.select_one('div.detail h2').get_text()
    start_finish = list(filter(lambda x: title[x] == '\n', range(len(title))))
    title = title[:int(start_finish[1])]
    title = title.replace(" ", "").replace("\n", "").replace("\t", "")
    
    last_page = bs.select_one('strong.page em').get_text() # 웹툰의 마지막 페이지
    url = url[:-4] 
    print('-' * 80 ,title, sep="\n", file = f)
    for i in range(1, int(last_page) + 1):
        url += str(i)
        title_list(url)
        url = url[:(len(str(i)) * -1)]
    print('-' * 80, "\n" *10, file= f)



url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url, headers= headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")


daily = soup.select('a.title') 
for web in daily:
    each_one("https://comic.naver.com" + web['href'][:-12])

f.close()