def profile(name, age, main):
    print("이름: {0}, 나이: {1}, 주 사용언어: {2} ".format(name, age, main))

profile("유재석", 20, "파이썬")
profile("조세호", 25, "자바")

print("")

# 등호를 사용하여 항목에 값이 주어지지 않았을때, 기본값을 설정할 수 있다
def profile2(name, age=30, main="파이썬"):
    print("이름: {0}, 나이: {1}, 주 사용언어: {2} ".format(name, age, main))

profile2("유재석")
profile2("조세호")
profile2("박명수", 25)