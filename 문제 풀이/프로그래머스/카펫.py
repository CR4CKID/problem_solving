"""
프로그래머스 > 완전탐색 > 카펫

맹점
    세로: x, 가로: y라 가정
    
    brown = 2(x+y-2)
    yellow = (x-2) * (y-2)
    
    yellow의 모든 경우의 수를 구한후 brown에 대입하여 맞는지 확인하는 방식
    
"""


def solution(brown, yellow):
    for i in range(1, yellow + 1):
        if yellow % i == 0 or yellow == i:
            if (yellow // i + i + 2) * 2 == brown:
                return [yellow // i + 2, i + 2]


print(solution(8, 1))
