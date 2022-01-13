import requests
from bs4 import BeautifulSoup
from selenium import webdriver



options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1920x1080')

options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36')

browser = webdriver.Chrome(options=options)
browser.maximize_window()
##################################################


url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'
browser.get(url)

detected_value = browser.find_element_by_id('detected_value')
print(detected_value.text)
browser.quit()

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
# HeadlessChrome/92.0.4515.131 Safari/537.36

# headless 사용 시 user agent에 headless가 포함되어 접속이 차단될 수 있음
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36')
# 따라서 이 문장이 필요