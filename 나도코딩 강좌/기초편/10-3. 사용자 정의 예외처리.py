class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    num = int(input("한자리 숫자를 입력하세요 " ))
    if num >= 10:
        raise BigNumberError("오류 발생")
except ValueError:
    print("잘못된 값을 입력하셨습니다.")
except BigNumberError as err:
    print("한자리수 값을 입력해야 합니다.")
    print(err)