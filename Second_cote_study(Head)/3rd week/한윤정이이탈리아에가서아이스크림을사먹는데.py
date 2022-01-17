'''
https://www.acmicpc.net/problem/2422
'''

import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().rstrip().split())

dont_mix = {i:[] for i in range(1,1+N)}
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    dont_mix[a].append(b)
    dont_mix[b].append(a)

result=0
for a in range(1,N+1):
    for b in range(a+1,N+1):
        if b in dont_mix[a]:
            continue
        for c in range(b+1, N+1):
            if c in dont_mix[a] or c in dont_mix[b]:
                continue
            result+=1

print(result)