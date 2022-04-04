'''
https://programmers.co.kr/learn/courses/30/lessons/42626

가장 낮은거 두개를 뽑아와야 하고,
만들어진것도 다시 넣어줘야한다.
heap이 필요할 것 같고,

2 ~ 백만
K는 10억까지
원소는 0~백만
K이상으로 만들 수 없으면 -1 리턴
'''

import heapq as hq

def solution(scoville, K):
    hq.heapify(scoville)
    answer = 0
    while len(scoville) >=2:
        if scoville[0] >= K:
            break
        a = hq.heappop(scoville)
        b = hq.heappop(scoville)
        result = a + b*2
        hq.heappush(scoville, result)
        answer += 1

    if scoville[0] < K:
        answer = -1
    return answer
scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))


