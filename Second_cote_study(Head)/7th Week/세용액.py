'''
https://www.acmicpc.net/problem/2473

산성 1 ~ 10억
알칼리 -1 ~ -10억
세가지 용액 섞어서 0에 가장 가까운 용액 만들기.
'''

import sys
input = sys.stdin.readline



def main():
    N = int(input().rstrip())
    liquids = sorted(list(map(int, input().rstrip().split())))
    result = solution(liquids)
    result = map(str,result)
    print(' '.join(result))

def solution(liquids):
    result_value = 3000000000
    for l in range(0,N-2):
        m, r = l+1, N-1
        while m < r:
            three = liquids[l] + liquids[m] + liquids[r]
            if abs(three) < result_value:
                result_value = abs(three)
                result = [liquids[l],liquids[m],liquids[r]]
                if result_value == 0:
                    break
            if three < 0:
                m += 1
            else:
                r -= 1
        if result_value ==0:
            break
    return result

if __name__ == '__main__':
    main()