# 몬티홀 문제 구현
list3 = []
for i in range(1000000):
    # 3개의 선택지 생성
    import random
    list1 = [True, False, False]
    list2 = [0,1,2]
    random.shuffle(list1)
    
    # 3개 중에 인덱스 한개 랜덤으로 설정
    num = random.randint(0,2)
    
    # 사회자가 염소가 있는 문을 오픈
    if list1[num] == False:
        open_num = list(filter(lambda x: list1[x] == False, range(len(list1))))
        open_num.remove(num) # 사회자가 여는 문 번호
    else:
        open_num = [list1.index(False)]
    
    # 참가자가 번호를 바꿈
    list2.remove(num)
    list2.remove(open_num[0])

    # 정답 or 오답
    if list2[0] == list1.index(True):
        list3.append(1)
    else:
        list3.append(0)

print(list3.count(1) / len(list3))