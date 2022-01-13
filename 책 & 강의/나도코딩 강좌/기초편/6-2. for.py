# for ... in 형식을 통하여 반복 구문을 만들 수 있다.
# range(@) 형식을 사용하면, 0부터 @ 전까지의 숫자를 생성한다.
# range(a, b) 형식을 통하여 시작 범위도 정할 수 있다.

for number in range (10):
    print("대기번호: {0}".format(number))

starbucks = ["아이언맨", "토르", "스파이더맨"]
for customer in starbucks:
    print("{0}님, 커피 나왔습니다.".format(customer))
