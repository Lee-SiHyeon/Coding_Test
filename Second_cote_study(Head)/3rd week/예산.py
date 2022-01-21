'''
https://www.acmicpc.net/problem/2512
'''

import sys
input = sys.stdin.readline

MIN_BUDGET = 1
MAX_BUDGET = 100000
N = int(input())
contries = list(map(int,input().rstrip().split()))
#내림차순 정렬
contries.sort(reverse = True)
budget = int(input())
sum_contries = sum(contries)

# 예산이 모든 나라 예산합보다 크면 max값 던져주면 됨.
if sum_contries <= budget:
    print( contries[0] )
else:
    #이진탐색 
    lp, rp = MIN_BUDGET, MAX_BUDGET
    mid = lp+(rp-lp)//2

    #나라들의 예산합 미리 계산해둠
    prefix_sum = [sum_contries]
    for i in range(1, N):
        prefix_sum.append(prefix_sum[i-1]-contries[i-1])

    while lp <= rp:
        # 탐색하는 국가 배정 예산이 국가예산들의 최대값보다 크면 탐색할 필요 없음.
        if mid > contries[0]:
            #탐색의 큰범위를 낮춤
            rp = mid-1

        # 탐색하는 국가 배정 예산이 국가예산들의 최소값보다 작은경우
        elif mid < contries[-1]:
            # 국가당 예산 * N개 국가 <= 예산 보다 작거나 같으면 mid를 키울 수 있음.
            if mid*N <= budget:
                lp = mid+1
            # mid*N만큼 돌려도 불가능함. 최소 예산신청한 국가조차 넘을 수 없음.
            # 이런경우 낮춰줘야함.
            else:
                rp = mid-1
        else:
            # mid가 contries의 max값 보다 작음.
            found = False
            for i, contry in enumerate(contries):
                if contry <= mid:
                    # i-1개가 mid보다 큼, 그만큼 mid만큼 배정해주고, 나머지는 그대로 가져갔을 때, 
                    # budget보다 작거나 같으면 사용가능한 최대 배정예산임.
                    if i * mid + prefix_sum[i] <= budget:
                        lp = mid +1
                        found = True
                        break            
            if found == False:
                rp = mid-1
        mid = lp+(rp-lp)//2
    print(mid)
