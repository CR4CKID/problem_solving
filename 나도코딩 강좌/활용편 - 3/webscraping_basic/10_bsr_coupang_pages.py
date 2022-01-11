import requests, re
from bs4 import BeautifulSoup



headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}



def item_check_inpage(url, n):
    url = url + '&page={}&'.format(n)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    global item_top10
    # 페이지 내 모든 아이템 추출 구문
    for item in soup.select('li.search-product'):
        if item.select_one('span.badge.rocket'):
            rating = item.select_one('.rating')
            rating_num = item.select_one('.rating-total-count')
            if rating:
                rating, rating_num = rating.get_text(), rating_num.get_text()[1:-1]
                name = item.select_one('.name').get_text()
                name = name[:name.find(',')]
                # 해당 아이템과 탑5 리스트 비교 구문
                if name in list(x[0] for x in item_top10):
                    continue

                if int(item_top10[0][3]) < int(rating_num):
                    # name = item.select_one('.name').get_text()
                    price = item.select_one('.price-value').get_text()
                    link = 'https://www.coupang.com' + item.select_one('a')['href']
                    # 같은 페이지 방지
                    item_top10[0] = [name,price,rating,rating_num,link]
                    # 탑5 리스트를 리뷰수에 따라 정렬
                    item_top10.sort(key= lambda x: int(x[3]))
                    

a = 0
stuff = input('검색 품목을 입력하세요: ')
url = 'https://www.coupang.com/np/search?component=&q=\
        {}&channel=user'.format(stuff)
item_top10 = [[0]*5]*5
for num in range(1,11):
    item_check_inpage(url, num)

# f = open('쿠팡 {} TOP5'.format(stuff), 'w', encoding='utf-8')
# 리스트 출력
item_top10 = item_top10[::-1]
for i, item in enumerate(item_top10):
    print(str(i+1) +'.','{0}\n{1}원, 평점: {2}, 리뷰 수: {3}\n링크: {4}\n\n\n'.format(\
        item[0], item[1], item[2], item[3], item[4]))
    

# f.close()