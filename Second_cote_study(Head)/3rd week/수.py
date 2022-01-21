'''
https://www.acmicpc.net/problem/22943
서로다른 두개의 소수 합
M으로 나눈 나머지가 
'''

import sys
from itertools import permutations,combinations
import math
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

sys.stdin = open('input.txt')
input = sys.stdin.readline

K,M = map(int,input().rstrip().split())

comb = list(permutations(range(10), K))
MAX_NUM = 10**K
primes = prime_list(MAX_NUM)

sum_primes = [False for _ in range(MAX_NUM)]
mul_primes = [False for _ in range(MAX_NUM)]
for i in range(len(primes)-1):
    for j in range(i+1, len(primes)):
        if primes[i]+ primes[j] < MAX_NUM:
            if sum_primes[primes[i]+primes[j]] == False:
                sum_primes[primes[i]+primes[j]] = True
        else:
            break
        
for i in range(len(primes)-1):
    for j in range(i, len(primes)):
        if primes[i] * primes[j] < MAX_NUM:
            if mul_primes[primes[i]*primes[j]] == False:
                mul_primes[primes[i]*primes[j]] = True
        else:
            break

result =0
results = []
for com in comb:
    if com[0] == 0:
        continue
    case = ''
    for c in com:
        case+= str(c)
    case = int(case)
    # 1번 조건. 서로다른 두개의 소수합인경우
    if sum_primes[case]:
        while True:
            if case%M ==0:
                case = case//M
            else:
                break
        if mul_primes[case]:
            result+=1
print(result)