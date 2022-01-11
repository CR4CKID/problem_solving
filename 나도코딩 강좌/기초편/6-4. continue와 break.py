absent = [2, 5]
nobook = [7]
for student in range(1, 11):
    if student in absent:
        continue # 아래 문장을 실행시키지 않고 다음 반복으로 넘어감
    elif student in nobook:
        print("오늘 수업은 여기까지. {0}번은 교무실로 따라와".format(student))
        break # 반복문 탈출
    print("{0}번, 책을 읽어봐".format(student))