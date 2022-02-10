"""
프로그래머스 > 완전탐색 > 소수 찾기
    
맹점
    
    크게 두 가지 파트 
        1. 각 숫자를 섞는 파트
             > 한 줄 for 문으로 숫자를 쪼갠후 
             > 숫자들의 조합을 만들어야함
                for문을 사용하여 조합을 만들려면 너무 복잡하지 않을까
                for문을 사용하더라도 여러자리의 숫자를 어캐 만들까
                    함수 내에 함수를 넣어서 하면 중복을 피할 수가 없음
                    
            itertools.permutations으로 해결
                    
        2. 섞어 만든 숫자가 소수인지를 확인하는 파트
        
    11과 011은 같은 숫자로 취급하므로 str을 int로 바꿔주기
    
"""
from itertools import permutations


def solution(numbers):
    arr = [n for n in numbers]
    prm = set()
    ans = 0

    def under_pri(n):
        if n <= 1:
            return 0
        for i in range(2, int(n ** 0.5 + 1)):
            if n % i == 0:
                return 0
        else:
            return 1

    for r in range(len(arr)):
        prm.update(set(map(int, map("".join, permutations(arr, r + 1)))))

    for n in prm:
        ans += under_pri(n)

    return ans


print(solution("011"))

