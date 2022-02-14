'''
https://www.acmicpc.net/problem/22942
0, 1, 2로 visited를 표기할건데,
0은 아무 영역도 아님,
1은 원 내부 표기
2는 원 반지름 표기.
'''

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
RANGE= 2000001
N = int(input())
circles = []
visited = [0 for i in range(RANGE)]
for _ in range(N):
    x, r = list(map(int,input().rstrip().split()))
    x = x+1000000 # X좌표 -100만 ~ 100만 인덱스 지원하기위해서.
    circles.append((x,r))
circles.sort(key = lambda x: x[0])
for x,r in circles:
    flag = True
    print(f'x = {x},r = {r}, visited[x] = {visited[x]}')
    if visited[x] == 0:
        if visited[x-r] ==0 and visited[x+r] == 0:
            for xx in range(x-r, x+r+1):
                if xx == x-r or xx == x+r:
                    visited[xx] = 2
                elif visited[xx] == 0:
                    visited[xx] = 1
        else:
            flag = False
            break
    elif visited[x] ==1:
        #원 안에 원을 그려야하는데 원을 벗어나면 안됨.
        for i in range(1, r+1):
            if visited[x+i] ==2 or visited[x-i] == 2:
                flag = False
                break
        visited[x-r], visited[x+r] = 2, 2
    elif visited[x] ==2:
        if visited[x-r] ==0 and visited[x+r] == 0:
            for xx in range(x-r, x+r+1):
                if xx == x-r or xx == x+r:
                    visited[xx] = 2
                elif visited[xx] ==0:
                    visited[xx] = 1
        else:
            flag = False
            break
    if flag == False:
        break
if flag == True:
    print("YES")
else:
    print("NO")