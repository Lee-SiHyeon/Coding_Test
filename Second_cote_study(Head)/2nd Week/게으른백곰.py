'''
https://www.acmicpc.net/problem/10025
'''
import sys
input = sys.stdin.readline

# (x좌표, 무게)로 input 받고, x좌표대로 정렬했습니다.
N, K = map(int,input().rstrip().split())
ices = []
for i in range(N):
    g, x =map(int,input().rstrip().split())
    ices.append((x,g)) # 뒤집어서 넣엇습니다.
ices.sort(key = lambda x: x[0]) # x좌표대로 오름차순 정렬

#계속 sum을 구해줘야 해서 prefix_sum을 미리 만들어뒀습니다.
prefix_sum = [0]
for x,g in ices:
    prefix_sum.append(prefix_sum[-1]+g)
prefix_sum = prefix_sum[1:]

'''
0 1 2 3 4 5 6 7
이고 k = 3이면
3을 택하면 0123456까지 택할 수 있다는건가
그러면 각 얼음을 가장 왼쪽으로 뒀을 때, 
0에 얼음이 있으면 k*2만큼 오른쪽으로 이동한 범위가 곰의 최대 범위
lp, rp(왼쪽 포인터, 오른쪽 포인터)를 두고 
lp,rp의 x좌표가 K*2 이내면 곰의 범위 내라서 sum을 구하고 max값 취함.
아직 곰의 범위 내라서 오른쪽 포인터(rp)를 늘려서 범위를 늘려나감

범위를 벗어났으면 lp를 오른쪽으로 옮겨서 범위를 좁힘.

prefix sum을 통해서 얼음 무게 합 구하는 시간을 줄임.
'''
result =0
lp, rp = 0,0

while lp <= rp and rp < N:
    lx, _ = ices[lp]
    rx, _ = ices[rp]
    if rx-lx <= K*2:
        sum = prefix_sum[rp]-prefix_sum[lp]+ices[lp][1]
        result = max(result, sum)
        rp+=1
    else:
        lp+=1    
print(result)