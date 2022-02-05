import requests, re
from bs4 import BeautifulSoup

f = open('쿠팡 리스트.txt', 'w', encoding='utf-8')

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

url = 'https://www.coupang.com/np/search?component=&q=\
    %EB%85%B8%ED%8A%B8%EB%B6%81&channel=user'
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

for item in soup.select('li.search-product'):
    badge_on = item.select_one('div.badges span')
    # if badge_on:
    #     print('추가할인은 제외합니다', '\n')  
    #     continue

    name = item.select_one('.name').get_text()
    price = item.select_one('.price-value').get_text()
    rating = item.select_one('.rating')
    rating_num = item.select_one('.rating-total-count')
    if rating and rating_num:
        rating, rating_num = rating.get_text(), rating_num.get_text()[1:-1]
        if float(rating) < 5 or int(rating_num) < 1000:
            continue
    else:
        continue
        rating, rating_num = "평점 없음","평점 없음"
    print(name, "\n" + price+'원', rating, rating_num, '\n', file= f)

f.close()