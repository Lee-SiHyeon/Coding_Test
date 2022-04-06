'''
https://programmers.co.kr/learn/courses/30/lessons/77485?language=python3

값들을 큐에 넣으면서 최소값 찾아놓고,
시작지점을 한칸 옮겨서 큐에 있는거 다시 잡아 넣으면 될거같은데,
쿼리가 10000개, 약 40개를 10000번 돌리면 ...
'''

from collections import deque

def solution(rows, columns, queries):
    dq = deque()
    board = [[0 for _ in range(columns)] for _ in range(rows)]

    value = 1
    for r in range(rows):
        for c in range(columns):
            board[r][c] = value
            value +=1
    answers = []

    for x1,y1,x2,y2 in queries:
        answer = 10001
        x1, y1, x2 , y2 = x1-1, y1-1, x2-1, y2-1
        # 윗 모서리 ( 좌 -> 우 )
        for c in range(y1, y2):
            dq.append(board[x1][c])
            answer = min(answer,board[x1][c])
        # 오른쪽 모서리 ( 상 -> 하 )
        for r in range(x1, x2):
            dq.append(board[r][y2])
            answer = min(answer,board[r][y2])
        # 아래모서리 ( 우 -> 좌 )
        for c in range(y2,y1,-1):
            dq.append(board[x2][c])
            answer = min(answer,board[x2][c])
        # 왼쪽 모서리 ( 하 -> 상)
        for r in range(x2,x1,-1):
            dq.append(board[r][y1])
            answer = min(answer, board[r][y1])
        
        answers.append(answer)
    
        for c in range(y1+1, y2+1):
            board[x1][c] = dq.popleft()
        for r in range(x1+1, x2+1):
            board[r][y2] = dq.popleft()
        for c in range(y2-1, y1-1,-1):
            board[x2][c] = dq.popleft()
        for r in range(x2-1,x1-1,-1):
            board[r][y1] = dq.popleft()

    return answers