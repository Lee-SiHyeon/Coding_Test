'''
https://www.acmicpc.net/problem/1238
N개의 마을마다 한명씩 학생이 살고있고
X마을을 왕복해야함.
각 마을 -> X마을로의 최단거리 계산 
X마을에서 각마을로의 최단거리 합 = 왕복 최단거리
'''
import sys
import heapq
input = sys.stdin.readline
INF = int(1e10)
def dijk(start):
    hq = []
    dist = [INF] * (N+1)
    heapq.heappush(hq,(0,start))
    while hq:
        d , now = heapq.heappop(hq)
        for next, cost in graph[now]:
            nc = d+ cost
            if nc < dist[next]:
                dist[next] = nc
                heapq.heappush(hq,(nc, next))
    return dist

N,M,X = list(map(int,input().rstrip().split()))
graph = [[] for i in range(N+1)]
for i in range(M):
    s, e, t = list(map(int,input().rstrip().split()))
    graph[s].append((e,t))

result = 0
for i in range(1,N+1):
    if i != X:
        go = dijk(i)
        back = dijk(X)
        result = max(result, go[X] + back[i])
print(result)