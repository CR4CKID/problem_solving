"""
프로그래머스 > 코딩테스트 연습 > 힙 > 디스크 컨트롤러

맹점
    하드 디스크가 작업을 수행하지 않을때는 다음 순서가 바로 수행됨
        즉 모든 순서를 마음대로 섞을 수는 없음
        처음 순서 또한 정해져 있음

    핵심요소: [요청시간, 소요시간], 실제 시작 시간
        요청 - 종료시간 = 실제시작시간 + 소요시간 - 요청시간
    
    굳이 요청 - 종료시간의 평균을 구하지 말고 더해가면서 min_time 변수를 선언하여 min_time을 넘어가면 break하여 소요시간을 단축시키는 방식
    
    주의할점
        하드디스크가 아무것도 안하고 있는 시간이 있을수도 있다

    형식 선택
        list : 요청 받은 목록들을 따로 모아둔 리스트
        deque : 처음 전달받은 목록들

    전달받은 리스트가 다 비워질때까지 반복문 수행
        중간값도 필요한 경우가 있을거 같으므로 리스트가 가장 합리적

    작업 리스트 = 요청 받은 목록들을 따로 모아둔 힙
        그 리스트에서 소요시간이 가장 적은 애를 먼저 시작
        전달받은 리슽트에서 time까지 popleft
            for문 사용?
        [소요시간, 요청시간]

구문

    time = 현재 시간
    min_times = 요청 - 종료시간 더한 값

    while (list와 deque가 존재할 동안):
        
        1. 요청받은 리스트에 요소가 존재할때
            - 존재 시 소요시간이 가장 적은 작업을 수행
                time += 소요시간
                min_time += (time - 요청시간)

            - 없을 때
                - 전체 리스트의 첫번째 요소의 시간이 time과 같으면
                    time += 소요시간
                - 다르면 
                    time = 첫번째 요소의 요청시간 + 소요시간
                전체리스트에서 첫번째 요소 제거
                min_time += 소요시간

        2. time 보다 작은 시간들을 작업 시간으로 옮김
            for문 사용
            작업리스트에는 [소요시간, 요청시간] 순서로 옮김
"""
import heapq as hq


def solution(jobs):
    num = len(jobs)
    min_times = 0
    time = 0
    ing_list = []
    jobs.sort()

    while ing_list or jobs:
        if ing_list:
            ing_job = hq.heappop(ing_list)
            time += ing_job[0]
            min_times += time - ing_job[1]
        else:
            if jobs[0][0] == time:
                time += jobs[0][1]
            else:
                time = jobs[0][0] + jobs[0][1]
            min_times += jobs[0][1]
            jobs.pop(0)

        for i, moving_job in enumerate(jobs):
            if moving_job[0] <= time:
                hq.heappush(ing_list, [moving_job[1], moving_job[0]])
            else:
                jobs = jobs[i:]
                break
        else:
            jobs = []
    return int(min_times / num)


print(
    solution(
        [
            [24, 10],
            [28, 39],
            [43, 20],
            [37, 5],
            [47, 22],
            [20, 47],
            [15, 34],
            [15, 2],
            [35, 43],
            [26, 1],
        ]
    )
)
