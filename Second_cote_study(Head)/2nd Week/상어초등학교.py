'''
https://www.acmicpc.net/problem/21608

N*N 격자
왼쪽 윗칸 (1,1) 상하좌우가 인접한 칸임
1. 인접칸에 좋아하는 학생이 많은 칸을 선호
2. 1이 여러개면 비어있는 칸이 가장 많은 칸으로 선택
3. 2를 만족하는것도 여러개면 행, 열 이 가장 작은 칸으로 ( 행우선 )
3<= N <= 20
'''
import sys
input = sys.stdin.readline

N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
students = []
dr = [-1, 0, 1, 0] # 상우하좌 (시계방향)
dc = [0, 1, 0 , -1]

#input 받기
for _ in range(N*N):
    info = list(map(int, input().rstrip().split()))
    student , prefer = info[0], info[1:]
    students.append((student, prefer))

# 입력받은 학생 순서대로
for stu, prefer in students:
    sorting_list = []
    for i in range(N):
        for j in range(N):
						#이미 다른 학생이 앉아있으면 스킵
            if board[i][j] != 0:
                continue
            # 비어있는 자리마다 탐색.
            prefer_cnt = 0
            blank_cnt = 0
						#4방향 탐색
            for k in range(4):
                nr, nc = i+dr[k] , j+dc[k]
                if 0<= nr<N and 0<= nc < N:
                    if board[nr][nc] in prefer:
                        prefer_cnt += 1
                    if board[nr][nc] == 0:
                        blank_cnt +=1
						#각 자리마다 결과를 저장해두고
            sorting_list.append((prefer_cnt, blank_cnt, i, j))
		# 탐색이 끝났으면 sorting함 
		# 선호학생 많은칸 / 빈자리 많은칸 / 윗줄 / 좌측줄 순서대로 정렬
    sorting_list.sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))
    r, c = sorting_list[0][2], sorting_list[0][3]
    board[r][c] = stu

sum = 0
students.sort(key = lambda x : x[0])
for i in range(N):
    for j in range(N):
        prefer_cnt =0
        for k in range(4):
            nr, nc = i+dr[k], j+dc[k]
            if 0<= nr<N and 0<= nc< N:
                if board[nr][nc] in students[board[i][j]-1][1]:
                    prefer_cnt +=1
        if prefer_cnt == 1:
            sum +=1
        elif prefer_cnt == 2:
            sum += 10
        elif prefer_cnt == 3:
            sum += 100
        elif prefer_cnt == 4:
            sum+=1000
print(sum)