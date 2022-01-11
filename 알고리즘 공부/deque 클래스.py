# deque : 앞 뒤쪽 방향에서 원소를 빠르게 추가하거나 제거할 수 있다.

# 일반적인 리스트가 양쪽 방향에서 원소를 제거하거나 추가할 때 연산에는 O(N)이 소요되지만,
    # (특정 원소에 접근하려면 처음이나 끝에서부터 선형 탐색을 하여야하기 때문에)
# deque는 O(1)로 접근이 가능하여 훨씬 빠르다.



# 컨테이너의 시작 / 끝 위치가 아닌 곳에서
# 삽입/제거 수행시 그 성능은 list에 비해 현저히 떨어진다.

from collections import deque

deq = deque()

# Add element to the start
deq.appendleft(10)

# Add element to the end
deq.append(0)

# Pop element from the start
deq.popleft()

# Pop element from the end
deq.pop()

'''
1. deque.append(item):      item을 데크의 오른쪽 끝에 삽입한다.
2. deque.appendleft(item):  item을 데크의 왼쪽 끝에 삽입한다.
3. deque.pop():             데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
4. deque.popleft():         데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
5. deque.extend(array):     주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
6. deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
7. deque.remove(item):      item을 데크에서 찾아 삭제한다.
8. deque.rotate(num):       데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).
'''

# ex)

# 5. extend와 append 비교
lst = ['a', 'b', 'c']
lst2 = ['a', 'b', 'c', 'd']
lst2.append('ef') # append()
lst.extend('ef') # extend()
print(lst) # ['a', 'b', 'c', 'd', 'e', 'f']
print(lst2) # ['a', 'b', 'c', 'd', 'ef']

    # deque에서도 동일하게 작용

# 8. rotate
deq = deque([1, 2, 3, 4, 5])
deq.rotate(1) # deque([5, 1, 2, 3, 4])
deq.rotate(-1) # deque([1, 2, 3, 4, 5])
print(deq)

