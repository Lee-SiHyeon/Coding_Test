'''
출발지점은 네 꼭지점에서 출발 시켜서
n-1칸, n-2칸 
5칸일때 4칸, 2칸, 1칸?
6칸일때 5칸 / 3칸 / 1칸
9칸일때 8칸 / 6칸 / 4칸 / 2칸 / 1칸
n칸일때 n-1칸에서 2칸씩 빼다가 , 마지막에 3칸남는지, 2칸남는지에 따라서 1칸 처리 해주면 될거 같은데?
'''


def solution(n, clockwise):
    board = [[ 0 for _ in range(n)] for _ in range(n)] # n*n
    start_points = [[0,0], [n-1, 0], [0, n-1], [n-1,n-1]]
    dx_dy= [[-1,0], [0, 1], [1,0], [0, -1]] #상 우 하 좌
    
    # false일때 -1 % 4해주면 되고,
    # true일때 +1 % 4해주면 됨
    true_start = [1, 0, 2, 3]
    false_start = [2, 1, 3, 0]
    
    for idx, start in enumerate(start_points):
        if clockwise:
            direction = 1
            dir = true_start[idx]
        else:   
            direction = -1
            dir = false_start[idx]
        cnt = n-1
        numbering = 1
        row, col = start[0], start[1]
        while cnt != -1:
            for i in range(cnt):
                board[row][col] = numbering
                numbering +=1
                if i != cnt-1:
                    row += dx_dy[dir][0]
                    col += dx_dy[dir][1]
            dir += direction
            dir = dir%4
            row += dx_dy[dir][0]
            col += dx_dy[dir][1]
            cnt -=2
            if cnt == 0:
                cnt = 1
    return board
        



        




def main():
    n = 6
    clockwise = False
    print(solution(n, clockwise))

main()