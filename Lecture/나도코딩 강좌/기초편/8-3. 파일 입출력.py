# 파일에 내용을 쓰기
# 형식: open("파일 이름", 사용 목적, encoding="utf8")
scorefile = open("score.txt", "w", encoding="utf8") # w: 덮어쓰기
print("수학은 60점", file=scorefile)
print("과학은 70점", file=scorefile)
scorefile.close()

scorefile = open("score.txt", "a", encoding="utf8") # a: 추가적으로 쓰기
scorefile.write("국어는 90점")
scorefile.write("\n사회는 30점") # \n: 줄바꿈
scorefile.close()

# 파일에 내용을 읽기

# 전체 읽기
scorefile = open("score.txt", "r", encoding="utf8")
print(scorefile.read()) # 파일 내 모든 내용 읽기
scorefile.close()

# 한줄만 읽기
scorefile = open("score.txt", "r", encoding="utf8")
print(scorefile.readline()) # 줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
print(scorefile.readline())
print(scorefile.readline())
print(scorefile.readline())

# 몇줄인지 모르는 파일 읽기: 반복문 사용
scorefile = open("score.txt", "r", encoding="utf8")
while True:
    line = scorefile.readline()
    if not line:
        break # 반복문 탈출
    print(line, end="")
scorefile.close()

# list 형태로 읽기
scorefile = open("score.txt", "r", encoding="utf8")
lines = scorefile.readlines()
for line in lines:
    print(line, end="")
scorefile.close()
