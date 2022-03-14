'''
https://programmers.co.kr/learn/courses/30/lessons/49189
1번에서 가장 먼 노드 구하기

bfs한번 돌리면 끝날듯
'''

from collections import deque

def solution(n, edge):
    visited = [False for i in range(n+1)]
    graph = [[] for _ in range(n+1)]

    for ed in edge:
        start , end = ed
        graph[start].append(end)
        graph[end].append(start)
    
    dq = deque()
    dq.append((1,0))
    visited[1] = True
    max_cost = 0
    answer = 1
    while len(dq):
        now, cost = dq.popleft()
        if cost > max_cost:
            answer = 1
            max_cost = cost
        elif cost == max_cost:
            answer += 1
        for next in graph[now]:
            if visited[next] == False:
                visited[next] = True
                dq.append((next, cost+1))
    
    return answer


def main():
    n = 6
    vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, vertex))

main()