# while: 특정 조건을 만족할 때 까지 반복
customer = "토르"
index = 5
while index >= 1:
    print("{0}님, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

customer = "아이언맨"
index = 1
while True:
    print("{0}님, 커피가 준비되었습니다. {1}번 호출".format(customer, index))
    index += 1

customer = "토르"
person = "a"
while person != customer:
    print("{0}님, 커피 나왔습니다.".format(customer))
    person = input("성함이 어떻게 되시나요? ")
    if person == customer:
        break
    print ("꺼지세요")
print("주문하신 커피 여기있습니다.")