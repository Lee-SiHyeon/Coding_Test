'''
https://programmers.co.kr/learn/courses/30/lessons/12973

100만
O(N^2)으로는 안될꺼고
바로바로 처리. stack 써서 top만 보면 2개는 처리가능함.
'''

def solution(s):
    stack = []
    for c in s:
        if not stack:
            stack.append(c)
        else:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
    if stack:
        return 0
    else:
        return 1

print(solution('cdcd'))