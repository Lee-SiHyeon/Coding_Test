'''
https://www.acmicpc.net/problem/11725
'''

import sys
from collections import deque
input = sys.stdin.readline

# input 받기
N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
dq = deque()
result = [0 for _ in range(N+1)]
for _ in range(N-1):
    s, e = map(int,input().rstrip().split())
    #양방향 그래프
    graph[s].append(e)
    graph[e].append(s)

# 1번노드를 시작점으로 시작.
dq.append(1)
visited[1] = True
while dq:
    node = dq.popleft()
    # 각노드에 연결된 노드로 이동할건데.
    for next_node in graph[node]:
        # 이미 간 곳이라면 갈 필요 없고.
        if not visited[next_node]:
            # 다음 갈 노드는 현재 노드가 부모이므로 표시 해주고 append
            result[next_node] = node
            visited[next_node] = True
            dq.append(next_node)

for i in result[2:]:
    print(i)

            


