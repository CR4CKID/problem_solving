# 사전 {key:value} 형식
cabinet = {3:"유재석", 10:"박명수"}

# 사전 자료형 가져오기
# 1.[] 사용, but 적합하지 않는 key 사용 시 오류 나면서 이어지지 않음 ex) print(cabinet[5])
print(cabinet[3])

# 2.get() 사용, 오류가 나더라도 계속 이어감 (none이라고 표기됨)
print(cabinet.get(3))

# 2-1. get() 사용 시 적합하지 않으면 도출되는 none 대신에 다른 기본 값 도출하는 법
print(cabinet.get(5, "기본값")) # get(*, "아무 기본값") 형식

# in을 사용하여 사전 자료형 안에 특정 값이 있는지 확인하는 방법
print(3 in cabinet) # True
print(5 in cabinet) # False

# 사전형에 값 추가 및 업데이트 하기
print(cabinet) # {3: '유재석', 10: '박명수'}
cabinet[3] = "조세호"
cabinet["abc"] = "정준하"
print(cabinet) # {3: '조세호', 10: '박명수', 'abc': '정준하'}

# del을 사용하여 사전형의 특정 값 삭제
print(cabinet) # {3: '조세호', 10: '박명수', 'abc': '정준하'}
del cabinet[3]
print(cabinet) # {10: '박명수', 'abc': '정준하'}

# 사전형의 key들만 출력
print(cabinet.keys())

# 사전형의 value들만 출력
print(cabinet.values())

# 사전형의 key와 value 모두 출력
print(cabinet.items())

# 사전형의 모든 값 제거
cabinet.clear()
print(cabinet)
