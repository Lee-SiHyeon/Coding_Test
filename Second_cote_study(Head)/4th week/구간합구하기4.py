'''
https://www.acmicpc.net/problem/11659
'''

import sys
input = sys.stdin.readline

N, M = list(map(int, input().rstrip().split()))
numbers = list(map(int, input().rstrip().split()))

prefix = [0, numbers[0]]
for idx, num in enumerate(numbers[1:]):
    prefix.append(prefix[idx+1]+num)

for _ in range(M):
    start, end = list(map(int,input().rstrip().split()))
    start -=1
    print(prefix[end]-prefix[start])
