'''
https://www.acmicpc.net/problem/10971
모든정점 지나야함.
'''
import sys
input = sys.stdin.readline

min_cost = int(1e10)
def dfs(start,cost,depth,finish):
    global min_cost

		# 코스트 예외처리 추가
    # 현재 cost가 glbal min_cost 보다 크다면 더이상 찾을 필요가 없다.
    if cost > min_cost:
        return
    if depth == N:
        min_cost = min(min_cost,cost)
        return
    if depth == N-1:
        if board[start][finish] != 0:
            dfs(finish,cost+board[start][finish],depth+1,finish)
        return
    for i in range(N):
        if visited[i] == False and board[start][i] !=0:
            visited[i] = True
            dfs(i,cost+board[start][i], depth+1,finish)
            visited[i] = False
    return
            
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int,input().rstrip().split())))
visited = [False] * N
for i in range(N):
    visited[i] = True
    dfs(i,0,0,i)
    visited[i] = False
print(min_cost)

