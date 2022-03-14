'''
https://programmers.co.kr/learn/courses/30/lessons/43238?language=python3

n 10억
심사시간최대 10억분
심사관 10만명

무조건 O(log) 시간복잡도..
N*log(N)? 도 안되겠는데
'''


def solution(n, times):
    answer = 1_000_000_000
    lp, rp = 0, 1_000_000_000
    mid = (lp+rp)//2
    times.sort()
    while lp <= rp:

        cnt = 0
        for time in times:
            cnt += mid //time
            if cnt > n:
                rp = mid-1
                break
        else:
            if cnt < n:
                lp = mid+1
            elif cnt == n:
                rp = mid-1
        print("lp, rp,mid, cnt = ", lp,rp, mid,cnt)
        mid = (lp+rp)//2
    
    return mid+1


def main():
    n = 6
    times = [7,10]
    print(solution(n, times))
main()