'''
https://www.acmicpc.net/problem/11399

각자 인출하는데 필요한 시간이 다름.
오름차순 정렬시켜서 구하면 될듯.
'''

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
times = list(map(int,input().rstrip().split()))
times.sort()
dp = [0]
for i, time in enumerate(times):
    dp.append(dp[i]+time)
print(sum(dp))