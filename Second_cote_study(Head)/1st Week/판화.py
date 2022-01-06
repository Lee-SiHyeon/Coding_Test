'''
https://www.acmicpc.net/problem/1730
N*N 격자에 점이 있음.
로봇의 위치는 항상 (0,0)
명령 순서가 주어지고 흔적을 출력하는 프로그램 작성
격자를 벗어나는 명령은 무시함.

UDLR로 표기.
board에서 로봇팔이 지나지 않은 곳은 '.', 수직으로 지나면 '|', 수평 '-', 수직 수평 모두는 '+'로 표기.
'''
import sys
input = sys.stdin.readline

N = int(input())
command = list(input().rstrip())
board = [['.' for _ in range(N)] for _ in range(N)]
dir = {
    'U' : (-1,0),
    'D' : (1,0),
    'R' : (0,1),
    'L' : (0,-1)
}
x,y = 0,0
for c in command:
    dx, dy = dir[c]
    nx, ny = x+dx, y+dy
    if 0 <= nx < N and 0 <= ny < N:
        if board[x][y] == '.':
            if c in ['U', 'D']:
                board[x][y] = '|'
            elif c in ['L','R']:
                board[x][y] = '-'
        elif board[x][y] == '|':
            if c in ['L','R']:
                board[x][y] = '+'
        elif board[x][y] == '-':
            if c in ['U','D']:
                board[x][y] = '+'

        if board[nx][ny] == '.':
            if c in ['U','D']:
                board[nx][ny] = '|'
            elif c in ['L','R']:
                board[nx][ny] = '-'
        elif board[nx][ny] == '|':
            if c in ['L','R']:
                board[nx][ny] = '+'
        elif board[nx][ny] == '-':
            if c in ['U','D']:
                board[nx][ny] = '+'
        x,y = nx,ny

for i in board:
    s = ''
    for c in i:
        s += c
    print(s)    