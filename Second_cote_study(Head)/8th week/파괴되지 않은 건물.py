'''
https://programmers.co.kr/learn/courses/30/lessons/92344?language=python3
0이하 파괴, 계속 감소될 수 있음.
type 1 : 공격, 2 : 회복
board : 1 <= N , M <= 1000 최대 1,000,000
skill : <= 25000
[type, r1, c1, r2, c2, degree]

최종적으로 1이상이면 파괴되지 않은 건물임.
'''
def solution(board, skill):
    N, M = len(board), len(board[0])
    queries = [[ 0 for _ in range(M+1)] for _ in range(N+1)]

    for sk in skill:
        type, r1, c1, r2, c2, degree = sk
        if type == 1:
            queries[r1][c1] -= degree
            queries[r2+1][c2+1] -= degree
            queries[r1][c2+1] += degree
            queries[r2+1][c1] += degree
        elif type == 2:
            queries[r1][c1] += degree
            queries[r2+1][c2+1] += degree
            queries[r1][c2+1] -= degree
            queries[r2+1][c1] -= degree
		#좌 -> 우 누적합
    for r in range(N+1):
        for c in range(1,M+1):
            queries[r][c] += queries[r][c-1]
		#우 -> 좌 누적합
    for r in range(1,N+1):
        for c in range(0, M+1):
            queries[r][c] += queries[r-1][c]

    answer =0
    for i in range(N):
        for j in range(M):
            board[i][j] += queries[i][j]
            if board[i][j] >0:
                answer +=1

    return answer