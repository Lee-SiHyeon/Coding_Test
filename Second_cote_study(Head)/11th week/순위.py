'''
https://programmers.co.kr/learn/courses/30/lessons/49191
'''
from collections import deque
def solution(n, results):
    result = 0
    go_graph = [[] for _ in range(n+1)] #0번 노드가 없음.
    back_graph = [[] for _ in range(n+1)] #0번 노드가 없음.
    parents = [-1 for _ in range(n+1)]
    children = [-1 for _ in range(n+1)]
    for winner, loser in results:
        go_graph[winner].append(loser) #
        back_graph[loser].append(winner)
    
    
    for i in range(1, n+1):
        visited = [False for _ in range(n+1)]
        dq = deque()
        dq.append(i)
        visited[i] = True
        cnt = 0
        while len(dq):
            node = dq.popleft()
            for next_node in go_graph[node]:
                if visited[next_node] == False:
                    visited[next_node] = True
                    dq.append(next_node)
                    cnt += 1
        visited = [False for _ in range(n+1)]
        dq.append(i)
        visited[i] = True
        while len(dq):
            node = dq.popleft()
            for next_node in back_graph[node]:
                if visited[next_node] == False:
                    visited[next_node] = True
                    dq.append(next_node)
                    cnt += 1

        if cnt == n-1:
            result += 1
    return result   