import requests
from bs4 import BeautifulSoup
from selenium import webdriver

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
 "Accept-Language":'ko-KR,ko'
 }

url = 'https://play.google.com/store/movies/top'

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 모니터의 해상도 높이인 1080 위치로 스크롤 내리기
#   browser.execute_script('window.scrollTo(0,1080)') # 1920 x 1080
#   browser.execute_script('window.scrollTo(0,2080)')

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

import time
interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

# 반복 수행
while True:
    # 스크롤을 가장 아래로
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height:
        break

    prev_height = curr_height

print('스크롤 완료')



res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(browser.page_source, 'lxml')

movies = soup.select('div.Vpfmgd')


for movie in movies:
    if movie.select('span.SUZt4c.djCuy'):
        print(movie.select_one('div.WsMG1c.nnK0zc').get_text())
        print(movie.select_one('span.VfPpfd.ZdBevf.i5DZme').get_text())
        print('https://play.google.com'+ movie.select_one('div.vU6FJ.p63iDd a')['href'])
        print('-' * 100)

browser.quit()