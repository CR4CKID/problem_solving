from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip # pyperclip을 임포트

url = 'https://naver.com/'
browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()

browser.find_element_by_class_name('link_login').click()
tag_id = browser.find_element_by_id('id') 
tag_pw = browser.find_element_by_id('pw')

uid = 'rlarl0240'
upw = 'Eogml0210!'

tag_id.clear()
tag_id.click()
pyperclip.copy(uid) # pyperclip을 통해 클립보드에 사용자 아이디 복제
tag_id.send_keys(Keys.CONTROL, 'v') # control + v를 통해 아이디 입력

tag_pw.clear()
tag_pw.click()
pyperclip.copy(upw)
tag_pw.send_keys(Keys.CONTROL, 'v')

browser.find_element_by_id('log.login').click()

browser.find_element_by_link_text('등록').click()