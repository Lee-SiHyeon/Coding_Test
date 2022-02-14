'''
https://www.acmicpc.net/problem/14567
'''
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    for root in roots:
        dq.append((root,1))
        results[root] = 1
    while dq:
        node, dist = dq.popleft()
        if node in board:
            for next in board[node]:
                need_visit[next] -= 1
                if need_visit[next] == 0:
                    dq.append((next,dist+1))
                    results[next] = dist+1


N, M = list(map(int, input().rstrip().split()))
board = {}
dq = deque()
need_visit = [0 for i in range(N+1)]
results = [0 for i in range(N+1)]
for _ in range(M):
    s, e = list(map(int, input().rstrip().split()))
    if s not in board:
        board[s] = [e]
    else:
        board[s].append(e)
    need_visit[e] +=1

# root 찾기
roots = []
for i in range(1,N+1):
    if need_visit[i] == 0:
        roots.append(i)
        
bfs()
results = map(str, results)
s = ' '.join(results)
print(s[2:])