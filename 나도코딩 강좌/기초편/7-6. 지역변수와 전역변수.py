# global을 사용하여 전역공간의 변수를 사용할 수 있다
# 일반적으로는 함수 내에서는 전역공간의 변수를 사용할 수 없다

gun = 10

def check(sol):
    gun = 20
    gun = gun - sol
    print(gun)

check(2)
print(gun) 

def check2(sol):
    global gun # 전역 공간의 gun 사용
    gun = gun - sol
    print(gun)

check2(2) # gun = 10을 사용

def checkreturn(gun,sol):
    gun = gun - sol
    return gun