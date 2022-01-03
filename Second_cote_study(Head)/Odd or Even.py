"""
https://www.acmicpc.net/problem/5747
둘의 손가락 합이 짝수가 나오면 메리가 승리하고,
둘의 손가락 합이 홀수가 나오면 존이 승리한다.

메리가 가장 최소로 승리할 횟수를 구해야함.
게임횟수 (N)- (짝/홀 + 홀/짝)  = 최소 값.

"""

import sys
sys.stdin = open('input.txt');
input = sys.stdin.readline
while True:
    N = int(input())
    if N == 0:
        break
    m_even, m_odd, j_even, j_odd = 0, 0 , 0, 0
    mary = list(map(int, input().rstrip().split()))
    john = list(map(int, input().rstrip().split()))
    for i in range(N):
        if mary[i] % 2 == 0:
            m_even += 1
        else:
            m_odd += 1
        if john[i] % 2 == 0:
            j_even += 1
        else:
            j_odd += 1
    print(N- min(m_even,j_odd)- min(m_odd, j_even))

    
    
