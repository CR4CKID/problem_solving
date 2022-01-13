"""
프로그래머스 > 스택/큐 > 주식가격

맹점
    핵심은 반복문을 최대한 적게 돌리는 것
        문제 해결 자체는 간단하지만 시간이 핵심
    

"""


def solution(prices):
    answer = []
    i = 0
    for num in prices[:-1]:
        i += 1

        if any(num > cur for cur in prices[i:]):
            for com in prices[i:]:
                if com < num:
                    answer.append(prices[i:].index(com) + 1)
                    break
        else:
            answer.append(len(prices) - i)
    answer.append(0)
    return answer


print(solution([1, 2, 3, 2, 3, 1, 3, 2]))
