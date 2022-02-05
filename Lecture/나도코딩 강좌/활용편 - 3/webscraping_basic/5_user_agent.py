import requests

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWe\
    bKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.277 Whale/2.9.118.38 Saf\
        ari/537.36'}
url = "http://nadocoding.tistory.com"
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text) 