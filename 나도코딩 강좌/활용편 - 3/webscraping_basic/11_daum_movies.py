from bs4 import BeautifulSoup
import requests

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}



for year in range(2015,2021):
    url = f'https://search.daum.net/search?w=tot&q=\
    {year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
    res = requests.get(url, headers= headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    images = soup.select('ol.type_plural.list_exact.movie_list img.thumb_img')
    for i, image in enumerate(images):
        image_url = image['src']
        image_res = requests.get(image_url, headers= headers)
        image_res.raise_for_status()

        with open('movie_{}_{}.jpg'.format(year, i), 'wb') as f: # 텍스트가 아닌 파일은 wb로 저장
            f.write(image_res.content)
 