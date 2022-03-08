'''
https://programmers.co.kr/learn/courses/30/lessons/43162
'''
from collections import deque
def solution(n, computers):
    visited = [False] * n
    answer = 0
    for i in range(n):
        dq = deque()
        if visited[i] == False:
            answer += 1
            visited[i] = True
            dq.append(i)
            while len(dq):
                now = dq.pop()
                for j in range(n):
                    if computers[now][j] == 1 and j != now and visited[j] == False:
                        visited[j] = True
                        dq.append(j)
    return answer

def main():
    n = 3
    computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    print(solution(n, computers))
main()
