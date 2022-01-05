'''
https://www.acmicpc.net/problem/16173
젤리는 아래, 오른쪽으로만 점프할 수 있고, 자신의 위치에 있는 숫자만큼만 움직일 수 있음.
0,0에서 출발해서 N-1,N-1에 도착하면 HaruHaru출력, 도착할 수 없는 board면은 Hing출력
'''

import sys
from collections import deque
input = sys.stdin.readline

# 아래, 오른쪽 순서
dr = [1, 0] 
dc = [0, 1]

# input
N = int(input())
board = []
dq = deque()
for _ in range(N):
    board.append(list(map(int,input().rstrip().split())))

# bfs
dq.append((0,0))
end = False
while dq:
    r, c= dq.popleft()
    step = board[r][c]
    # 못 움직이므로 예외처리
    if step == 0:
        continue
    # 도착하면 end Flag 세우고 while 종료
    if r == N-1 and c == N-1 and step == -1:
        end = True
        break
    # 아래, 오른쪽 움직이기
    for i in range(2): 
        nr, nc = r+ dr[i]*step, c+dc[i]*step
        if 0<= nr <= N-1 and 0<= nc <= N-1:
            dq.append((nr,nc))

if end: print("HaruHaru")
else: print("Hing")
    
