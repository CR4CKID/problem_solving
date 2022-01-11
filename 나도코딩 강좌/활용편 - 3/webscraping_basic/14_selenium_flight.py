import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = 'https://flight.naver.com/flights/'
browser.get(url) # url로 이동

# 가는 날 클릭
browser.find_element_by_link_text('가는날 선택').click()


# 이번달 28, 29일 선택
# browser.find_elements_by_link_text('28')[0].click()
# browser.find_elements_by_link_text('29')[0].click()

# 다음달 28, 29일 선택
# browser.find_elements_by_link_text('28')[1].click()
# browser.find_elements_by_link_text('29')[1].click()

# 이번달 28일, 다음달 29일 선택
browser.find_elements_by_link_text('28')[0].click()
browser.find_elements_by_link_text('29')[1].click()

# 제주 선택
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]').click()

# 항공군 검색 클릭
# browser.find_element_by_xpath('//*[@id="searchArea"]/a').click()
browser.find_element_by_link_text('항공권 검색').click()

# 브라우저를 최대 10초까지 대기하면서 xpath를 기준으로 해당하는 값이 나올때까지 대기
try:
    elem = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    print(elem.text) # 첫번째 결과 출력
finally:
    browser.quit()


# 첫번째 결과 출력
# elem = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')
# print(elem.text)