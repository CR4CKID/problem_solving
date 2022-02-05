import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}


# 오늘의 날씨
url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8&oquery=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0&tqi=het1Cwp0JXossg0ANlossssstHV-398783'
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

info = soup.select_one('div.info_data')
print('[오늘의 날씨]')
print(info.select_one('.cast_txt').get_text()) # 날씨 & 어제와 온도 비교
curr_temp = info.p.get_text()
min_max = info.select_one('.merge').get_text()
print(f'현재 {curr_temp[:2]}{curr_temp[-2]}  (최저: {min_max[1:4]}\
 / 최고: {min_max[-3:]})') # 현재 온도 & min_max
rain_rate = soup.select_one('.date_info.today').select('.rain_rate')
print(f'오전 {rain_rate[0].get_text()[1:]} / 오후 {rain_rate[1].get_text()[1:]}')

# 헤드라인 뉴스
url = 'https://news.naver.com/'
res = requests.get(url, headers= headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

print('\n[헤드라인 뉴스]')
news = soup.select('.hdline_article_tit')
for i, new in enumerate(news):
    link = new.a['href']
    print(f'{i+1}. {new.a.get_text().strip()}\n (링크: https://news.naver.com{link})')

# IT 뉴스
url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105'
res = requests.get(url, headers= headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')
print('\n[IT 헤드라인 뉴스]')
it_news = soup.select_one('._persist').select('.cluster_list')
for i, it in enumerate(it_news):
    title = it.select_one('.cluster_text').a.get_text().strip()
    link = it.a['href']
    print(f'{i+1}. {title}\n (링크: https://news.naver.com{link})')

# 해커스 영어회화
url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english'
res = requests.get(url, headers= headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')
print('\n[해커스 매일 영어회화 학습]')

for txts in soup.select('.conv_txt'):
    print(txts.b.get_text())
    for txt in txts.select('div'):
        print(txt.get_text().strip())
    print('\n')