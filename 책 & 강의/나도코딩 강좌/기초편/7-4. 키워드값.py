# 키워드를 사용하여 함수의 값을 호출할 수 있다.
def profile(name, age, main):
    print("이름: {0}, 나이: {1}, 주 사용언어: {2} ".format(name, age, main))

profile("유재석", 20, "파이썬")
profile(main="파이썬", name= "유재석", age = 20)