# if, elif, else 후 :(콜론) 사용
# and나 or를 사용하여 추가적인 조건을 사용할 수 있다.
weather = input("오늘 날씨는 어때요? ")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 노 필요요")

# input()은 문자이므로 int(input())을 통해 숫자로 변환 가능
temp = int(input("오늘 기온이 어떻게 되나요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요.")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨네요.")
elif 0 <= temp < 10:
    print("조금 쌀쌀하네요. 외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요.")