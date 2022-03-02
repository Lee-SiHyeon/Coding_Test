'''
https://programmers.co.kr/learn/courses/30/lessons/12904
'''

def solution(s):
    maximum = 1
    if len(s) == 0 or len(s) == 1:
        return len(s)
    for i in range(len(s)):
        idx = [(i,i), (i, i+1)]
        for l,r in idx:
            cnt = 0
            while 0<=l and r <= len(s)-1:
                if l==r:
                    cnt += 1
                    l ,r = l-1, r+1
                    continue
                elif s[l] == s[r]:
                    cnt += 2
                    l ,r = l-1, r+1    
                else:
                    break
            maximum = max(maximum, cnt)
    return maximum