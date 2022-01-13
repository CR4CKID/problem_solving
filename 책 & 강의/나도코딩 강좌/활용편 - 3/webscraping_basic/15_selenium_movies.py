import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
 "Accept-Language":'ko-KR,ko'
 }

url = 'https://play.google.com/store/movies/top'
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

movies = soup.select('div.ImZGtf.mpg5gc')
print(len(movies))

for movie in movies:
    print(movie.select_one('div.WsMG1c.nnK0zc').get_text())