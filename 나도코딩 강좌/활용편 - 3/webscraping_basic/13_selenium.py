import time
from selenium import webdriver

browser = webdriver.Chrome() # () 안에 드라이버 위치 명시, 같은 경로에서는 필요 X

# 1. 네이버로 이동
browser.get('http://naver.com')

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name('link_login')
elem.click()

# 3. id, pw 입력
browser.find_element_by_id('id').send_keys('rlarl0240')
browser.find_element_by_id('pw').send_keys('Eogml0210!')

# 4. 로그인 버튼 클릭
browser.find_element_by_xpath('//*[@id="log.login"]').click()

time.sleep(3)

# 5. id, pw 재입력
browser.find_element_by_id('id').clear()
browser.find_element_by_id('id').send_keys('rlarl0240')
browser.find_element_by_id('pw').send_keys('Eogml0210!')

# 6. html 정보 출력
print(browser.page_source) # 페이지의 모든 html 요소를 출력

# 7. 브라우저 종료
browser.quit() # 전체 종료
# browser.close() 현재 창 종료