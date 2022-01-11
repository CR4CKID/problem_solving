# sorted()는 리스트를 특정 key를 기준으로 정렬하여 반환하는 함수이다


# 1
# word에서 key를 기준으로 정렬, find를 사용할때 괄호 없이 사용
word = "abbccdda"
print(sorted(word,key=word.find)) # ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd']

# 2
# 사전에서 key나 value를 기준으로 정렬도 가능
myDict = {3:1,2:3,1:2}
print(sorted(myDict.items(), key= lambda x: x[0])) # [(1, 2), (2, 3), (3, 1)] key 기준
print(sorted(myDict.items(), key= lambda x: x[1])) # [(3, 1), (1, 2), (2, 3)] value 기준

# 3
# reverse= 를 사용하여 오름차순, 내림차순으로 정렬 가능
print(sorted(range(1,10),reverse=True)) # [9, 8, 7, 6, 5, 4, 3, 2, 1], 내림차순
print(sorted(range(1,10),reverse=False)) # [1, 2, 3, 4, 5, 6, 7, 8, 9], 오름차순

# 4
# 튜플을 사용하여 여러 조건을 동시에 정렬 가능
list3 = [[1,-1], [1,5], [2,-2], [3,-5], [3, 2], [3,1]]
print(sorted(list3, key= lambda x:(x[0], x[1]))) 
# [[1, -1], [1, 5], [2, -2], [3, -5], [3, 1], [3, 2]]
# x[0]으로 먼저 정렬한 후 x[1]로 정렬