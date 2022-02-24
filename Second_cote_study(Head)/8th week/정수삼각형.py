'''
https://programmers.co.kr/learn/courses/30/lessons/43105
'''
def solution(triangle):
    n, m = len(triangle), len(triangle[-1])
    board = [[0 for _ in range(m)] for _ in range(n)]
    board[0][0] = triangle[0][0]
    for i in range(1,n):
        for j in range(i+1):
            if j == 0:
                board[i][j] = triangle[i][j] + board[i-1][j]
            elif j == n:
                board[i][j] = triangle[i][j] + board[i-1][j-1]
            else:
                board[i][j] = triangle[i][j] + max(board[i-1][j-1], board[i-1][j])
    return max(board[-1])