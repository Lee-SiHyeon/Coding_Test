'''
https://programmers.co.kr/learn/courses/30/lessons/60059?language=python3

열쇠는 회전 이동 가능
돌기 부분을 홈과 딱맞게 채우면 열림

key는 M*M(M은 3 ~ 20) 
lock은 N*N(N은 3 ~ 20)
돌리기도 하고 움직일 수도 있는거면..

일단 돌리는거 가짓수 4개
움직이는건.. N*N에 .. 각 위치마다 M*M을 연산해줘야하면..
20*20 *20*20 = 16만 
16만 * 4 = 64만
완전탐색으로 가능할듯.

\return True or False
'''

def solution(key, lock):
    def turn_matrix(matrix):
        tmp = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                tmp[j][len(matrix)-1-i] = matrix[i][j]
        return tmp
    n = len(lock)
    m = len(key)
    new_lock = [[1 for _ in range(n+m-1)] for _ in range(n+m-1)]
    answer_count = 0
    for i in range(m-1,n+m-1):
        for j in range(m-1,n+m-1):
            new_lock[i][j] = lock[i-(m-1)][j-(m-1)]
            if new_lock[i][j] == 0:
                answer_count += 1
    for i in new_lock:
        print(i)
    for _ in range(4):
        for r in range(n+m-1):
            for c in range(n+m-1):
                #각 lock 원소들에 대해서 key를 맞춰볼거임.
                flag = True # 맞다는 가정하에 시작
                count = 0
                for rr in range(m):
                    for cc in range(m):
                        if r+rr >= m-1 and r+rr < n+m-1 and c+cc >= m-1 and c + cc < n+m-1:
                            if (key[rr][cc] == 1 and new_lock[r+rr][c+cc] == 1) or \
                                (key[rr][cc] == 0 and new_lock[r+rr][c+cc] == 0):
                                # 키가 돌기이고, lock도 돌기이면 불가능
                                # 키가 홈인데, lock도 홈이면 모든 홈을 채울 수 없으니까.
                                flag = False
                                break
                            elif key[rr][cc] == 1 and new_lock[r+rr][c+cc] == 0:
                                count +=1
                    #잘못맞춰진 경우 빠져나오고
                    if flag == False:
                        break
                #다 돌았는데, True인 상태이면 들어맞는 것
                if flag == True and count == answer_count:
                    print('r,c = ', r, c)
                    return True
        #위에서 return안났으면 맞춰지지 않은거니까 키를 돌려줌
        # range(3) = 0, 1, 2 
        # 시작때 주어진대로 하고 , 90도 , 180, 270도 돌려서 한번씩.
        key = turn_matrix(key)
    return False   

key, lock = [[0, 0, 0],[0, 0, 1],[0, 1, 0]], [[1, 1, 1],[0, 1, 1],[1, 1, 1]]
    
print(solution(key, lock))
