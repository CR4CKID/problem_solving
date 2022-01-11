# def profile(name, age, lang1, lang2, lang3, lang4):
#     print("이름: {0}, 나이: {1}".format(name, age), end=" ") # end=" " 사용 시 줄바뀜 없음
#     print("주 사용언어:", lang1, lang2, lang3, lang4)
# 위 함수는 주 사용언어의 개수가 바뀌면 함수 자체를 바꿔야 하기때문에 사용하기 불편하다

# *을 사용하여 가변인자 활용
def profile(name, age, *lang):
    print("이름: {0}, 나이: {1}".format(name, age), end=" ") # end=" " 사용 시 줄바뀜 없음
    for language in lang:
        print(language, end=" ")
    print()

profile("유재석", 25, "Python", "Java", "C", "C++")
profile("조세호", 20, "Swift", "Kotlin", "Java")