import requests
from bs4 import BeautifulSoup
from requests.api import head

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

url = 'https://comic.naver.com/index'
res = requests.get(url, headers= headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title.get_text())
print(soup.a)         # soup 객체에서 처음 발견되는 a element 출력
print(soup.a.attrs)   # a element의 속성 정보를 출력
print(soup.a['href']) # a element의 href 속성 '값' 정보를 출력

# class가 webtoon_corp_info인 a element를 찾음
print(soup.find('div', attrs = {'class': 'webtoon_corp_info'}).get_text())

rank1 = soup.find('li', attrs = {'class': 'rank01'})
print(rank1.a.text)

# next_sibling
print(rank1.next_sibling)
print(rank1.next_sibling.next_sibling)  # 랭크 사이에 공백이 있을 수 있다

rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())

# previous_sibling
rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())

# parent
print(rank1.parent)

# find_next_sibling / find_previous_sibling
rank2 = rank1.find_next_sibling('li')
print(rank2.a.get_text())
rank3 = rank2.find_next_sibling('li')
print(rank3.a.get_text())
rank2 = rank3.find_previous_sibling('li')
print(rank2.a.get_text())

# find_next_siblings
for rank in rank1.find_next_siblings('li'):
    print(rank.a.get_text())

# find(text=)
webtoon = soup.find("a", text= '더 복서-83화 전투(2)')
print(webtoon)