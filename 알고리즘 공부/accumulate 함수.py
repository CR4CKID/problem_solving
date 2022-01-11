# 누적된 합을 도출하는 함수
# for문으로 합하는것보다 훨씬 빠름

from itertools import accumulate

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = list(accumulate(list1))
print(list2)