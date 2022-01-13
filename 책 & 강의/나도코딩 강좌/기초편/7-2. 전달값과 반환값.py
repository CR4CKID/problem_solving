# 함수의 괄호 사이에 전달할 값을 넣는다
# 반환값은 return을 사용한다
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다. ".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다. ".format(balance - money))
        return balance - money
    else:
        print("잔액이 부족합니다.")
        return balance

def withdraw_night(balance, money):
    commission = 100 # 수수료
    return commission, balance - money - commission # 튜플 형식, 콤마로 구분 
balance = 0
balance = deposit(balance, 1000)
print(balance)

balance = withdraw(balance, 500)
print(balance)

commission, balance = withdraw_night(balance, 200)
print("수수료는 {0}원이며, 잔액은 {1}원 입니다. ".format(commission, balance))