import requests
from bs4 import BeautifulSoup
from selenium import webdriver


# 백그라운드에서 크롬 실행
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1920x1080')

browser = webdriver.Chrome(options=options)
browser.maximize_window()
##################################################

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
 "Accept-Language":'ko-KR,ko'
 }

url = 'https://play.google.com/store/movies/top'
browser.get(url)

import time
interval = 2
prev_height = browser.execute_script('return document.body.scrollHeight')
while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(interval)
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height:
        break
    prev_height = curr_height
print('스크롤 완료')

# 진행상황을 확인하기 위한 스크린샷
browser.get_screenshot_as_file('google_movie.png')




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