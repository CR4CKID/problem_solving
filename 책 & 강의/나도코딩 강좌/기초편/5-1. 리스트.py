# 리스트 []로 묶어 사용

subway = [10,20,30]
print(subway)

subway = ["유재석", "박명수", "조세호"]
print(subway)

# 박명수가 몇번째 칸에 타고 있는가
print(subway.index("박명수"))

# append를 사용하여 리스트 맨 뒤에 항목 추가 가능
subway.append("하하")
print(subway)

# insert(index, 객체 순서)를 사용하여 리스트 중간에 항목 추가 가능
subway.insert(1, "정형돈")
print(subway)

# pop을 사용하여 리스트 맨 뒤 항목 제거
print(subway.pop()) # pop을 통해 제거한 항목 확인
print(subway)

# count를 사용하여 리스트에 같은 항목이 얼마나 있는지 확인
subway.append("유재석")
print(subway.count("유재석"))

# sort를 사용하여 정렬 가능
list = [7,4,5,6,2,1,3]
list.sort()
print(list)

# reverse를 사용하여 순서 뒤집기 가능
list.reverse()
print(list)

# clear를 사용하여 리스트 내 항목 제거 가능
list.clear()
print(list)

# 리스트는 다양한 자료형 사용 가능
list2 = ["유재석", 20, True]
print(list2)

# extend를 사용하여 리스트 병합 가능
list1 = [1,2,3,"박명수"]
list2.extend(list1)
print(list2)