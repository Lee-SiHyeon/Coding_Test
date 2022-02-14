'''
https://www.acmicpc.net/problem/14620
씨앗 3개, 상하좌우/중앙


'''
import sys
from itertools import combinations
import copy
input = sys.stdin.readline

# dx = [-2,-1,-1,-1,0,0,0,0,0,1,1,1,2]
# dy = [0,-1,0,1,-2,-1,0,1,2,-1,0,1,0]
cost_dx = [-1,0,0,0,1,-2,-1,-1,0,0,1,1,2] # 4번인덱스까지 cost합쳐야함.
cost_dy = [0,-1,0,1,0,0,-1,1,-2,2,-1,1,0]

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int,input().rstrip().split())))

def check_visit(r,c,visited,cost):
    for i in range(len(cost_dx)):
        nr,nc = r + cost_dx[i] , c + cost_dy[i]
        if i <= 4:
            cost += board[nr][nc]
        if 0<=nr<N and 0<=nc<N:
            visited[nr][nc] = True
    return cost

result = int(1e9)
for ar in range(1,N-1):
    for ac in range(1,N-1):
        visited_a = [[False for i in range(N)] for j in range(N)]
        cost_a = 0
        cost_a += check_visit(ar,ac,visited_a,cost_a)
        for br in range(ar,N-1):
            for bc in range(1, N-1):
                if visited_a[br][bc] == True:
                    continue
                visited_b=copy.deepcopy(visited_a)
                cost_b = cost_a
                cost_b = check_visit(br,bc,visited_b,cost_b)
                for cr in range(br, N-1):
                    for cc in range(1, N-1):
                        if visited_b[cr][cc] ==True:
                            continue
                        visited_c=copy.deepcopy(visited_b)
                        cost_c = cost_b
                        cost_c = check_visit(cr,cc,visited_c,cost_c)
                        result = min(result, cost_c)
print(result)