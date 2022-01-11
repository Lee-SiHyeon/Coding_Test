'''
https://www.acmicpc.net/problem/2579
한번에 한계단 혹은 두계단 오를 수 있음.
연속된 세개의 계단을 밟아서는 안됨.
'''

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
stairs = []
for _ in range(N):
    stairs.append(int(input()))
dp = [0 for _ in range(N+1)]

for i in range(1,N+1):
    #첫 계단과 두번쨰 계단 밟음.
    if i==1:
        dp[i] = stairs[i-1]
    elif i==2:
        dp[i] = stairs[i-2]+stairs[i-1]

    #세번째 계단은 두가지 경우의 수에서 선택함.
    # 첫번쨰 계단을 밟고 2칸을 뛰어 3번째 계단을 밟던지
    # or 두번째 계단을 밟고 3번째 계단을 밟던지.
    elif i==3:
        dp[i] = max(stairs[i-3]+stairs[i-1], stairs[i-2]+stairs[i-1])
    
    #나머지 계단들은 두칸 뛰어서 접근 할수도 있고, 이전 계단을 밟고 접근 할 수 있음.
    # 전자는 두칸전까지 계단 합과 현재 칸을 합치면 되고,
    # 후자는 3칸 전까지 계단 합과 1칸전 계단수와 현재 칸을 합치면 된다.
    else:
        dp[i] = max(dp[i-2]+stairs[i-1] , dp[i-3] + stairs[i-2]+stairs[i-1])
    print(dp)
print(dp)

