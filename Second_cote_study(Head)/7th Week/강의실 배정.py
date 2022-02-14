'''
https://www.acmicpc.net/problem/11000
'''

import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline
N = int(input())
times = []
for _ in range(N):
    times.append(list(map(int,input().rstrip().split())))

times.sort()
rooms = [] #endtime 저장용

for i, time in enumerate(times):
    start, end = time
    if len(rooms) == 0:
        rooms.append(end)
    else:
        if start >= rooms[0]:
            heapq.heappop(rooms)
            heapq.heappush(rooms, end)
        else:
            heapq.heappush(rooms,end)
print(len(rooms))
