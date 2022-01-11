# Quiz) 사이트 별로 비밀번호를 만들어주는 프로그램을 작성하시오.

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 → naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 → naver
# 규칙3 : 남은 글자 중 처음 세 자리 + 글자 갯수 + 글자 내 'e'의 갯수 + '!'로 구성
#                        (nav)                      (5)                   (1)             (!)


site = "http://google.com"
num1 = site[7:site.find(".")] #naver
count = len(num1) #글자 개수
ecount = num1.count("e") #e의 개수
print(num1[:3] + str(count) + str(ecount) + "!")

site = "http://google.com"
num1 = site.replace("http://", "")
num1 = num1[0:num1.find(".")]
password = num1[:3] + str(len(num1)) + str(num1.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다".format(site, password))