print("java", "python") # java python
print("java" + "python") # javapython

# 콤마 사이에 sep="" 형식을 사용하여 원하는 문자를 넣을 수 있다
print("java", "python", sep=(",")) # java,python
print("java", "python", "C+", sep=(" vs ")) # java vs python vs C+

# end=("") 형식을 사용하여 문자의 마지막에 줄바뀜 대신 다른 문자를 삽입하여 줄바뀜을 없애준다
print("python", "java", sep=(", "), end=("? "))
print("무엇이 더 재밌을까요?") # python, java? 무엇이 더 재밌을까요?

# .ljust(@), .rjust(@)를 통해 @칸을 공간에서 좌우로 정렬 가능
score = {"수학": 0, "국어": 50, "과학": 100}
for subject, score in score.items():
    print(subject, score)

score = {"수학": 0, "국어": 50, "과학": 100}
for subject, score in score.items():
    print(subject.ljust(2), str(score).rjust(3), sep=(": "))

# .zfill(@) 형식을 통해 @만큼의 공간을 확보하고 공간이 비어있을 시 0으로 채움
for num in range(1,21):
    print(str(num).zfill(3))

# input을 사용하여 표준입력 활용        주의점: input은 항상 문자열 형태로 저장된다
answer = input("아무 값이나 입력하세요 ")
print("입력하신 값은 {0}입니다.".format(answer))