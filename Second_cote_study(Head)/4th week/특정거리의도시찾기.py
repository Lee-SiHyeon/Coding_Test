'''
https://www.acmicpc.net/problem/18352
'''

import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, K, X = list(map(int, input().rstrip().split()))
board = {}
dq = deque()
visited = [False for _ in range(N+1)]
result =[]
for i in range(M):
    s, e = list(map(int, input().rstrip().split()))
    if s not in board:
        board[s] = [e]
    else:
        board[s].append(e)

dq.append((X, 0))
visited[X] = True

while dq:
    nowNode, sum = dq.popleft()
    print(nowNode, sum)
    if sum == K:
        result.append(nowNode)
    if nowNode in board:
        for next in board[nowNode]:
            if visited[next] == False:
                dq.append((next,sum+1))
                visited[next] = True

if len(result) == 0:
    print(-1)
else:
    result.sort()
    for re in result:
        print(re)