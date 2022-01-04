'''
https://www.acmicpc.net/problem/2891
카약과 강풍

부서진 팀과 여분이 있는팀이 있음.
그런데 부서진 팀이 여분이 있는경우를 제외 해 주고
오름차순 정렬해서 하나씩 비교해가면서 result를 하나씩 빼줌.
'''

import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input
N, S, R = list(map(int, input().rstrip().split()))
broken = list(map(int, input().rstrip().split()))
one_more = list(map(int,input().rstrip().split()))

# 교집합(부서진 팀 & 여분이 있는팀) 정리
tmp =list(set(broken) & set(one_more))
broken = list(set(broken) - set(tmp))
one_more = list(set(one_more) - set(tmp))

# 정렬
broken.sort()
one_more = sorted(one_more)
one_more = deque(one_more) #여분이 있는팀이 나눠줬으면 pop하려고.
result = len(broken) #최초 출발 불가능한 팀 수 
for i in broken:
    if one_more:
        for j in one_more:
            if i +1 == j or i-1 == j:
                result -= 1 #나눠주는게 가능하면 불가능한 팀 수를 1씩 줄임.
                one_more.popleft();
                break
print(result)
            