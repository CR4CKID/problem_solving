import csv
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=' 

# csv 파일 작성
filename = '시가총액 1-200.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='') 
    # newline을 통해 줄바뀜을 없앨수 있다
    # 엑셀 파일에서 한글이 깨질 시 인코딩을 utf-8-sig로 하면된다.
writer = csv.writer(f)

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

title = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE'.split('\t')
# strip()을 사용하여 string의 탭 간을 나누고 리스트로 저장
writer.writerow(title)

for page in range(1,6):
    res = requests.get(url + str(page), headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    # if page == 1:
    #     titles = [title.get_text() for title in soup.select('thead tr th')]
    #     writer.writerow(titles)

    rows = soup.select('table.type_2 tbody tr')
    for row in rows:
        if len(row) <= 1: # 의미 없는 데이터 스킵
            continue
        datas = [data.get_text().strip() for data in row.select('td')]
        # print(datas)
        writer.writerow(datas) # writerow에 리스트를 넣으면 된다. 