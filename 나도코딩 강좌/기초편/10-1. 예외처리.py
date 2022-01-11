try:
    print("나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자 : "))
    num2 = int(input("두 번째 숫자 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # 에러 문장을 바로 출력할 수 있음
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생했습니다.") # 나머지 모든 에러 출력 가능