# raise를 사용하여 에러를 발생시킬 수 있다.
try:
    num = int(input("한자리 숫자를 입력하세요 " ))
    if num >= 10:
        raise ValueError

except ValueError:
    print("잘못된 값을 입력하셨습니다.")