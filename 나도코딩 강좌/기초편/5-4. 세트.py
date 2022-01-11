# 집합(set) {}, set([]) 두 형식 모두 가능
# 중복 안됨, 순서 없음
set1 = {1,2,3,3,3}
print(set1) # {1,2,3}

# 교집합: & or intersection() 형식
java = {"유재석", "박명수", "양세형"}
python = set(["유재석", "조세호"])
print(java & python)
print(java.intersection(python))

# 합집합: | or union() 형식
print(java | python)
print(java.union(python))

# 차집합: - or difference() 형식
print(java - python)
print(java.difference(python))

# add()와 remonve()를 사용하여 세트 내 항목 추가 및 제거
java.add("김태호")
print(java)
java.remove("양세형")
print(java)