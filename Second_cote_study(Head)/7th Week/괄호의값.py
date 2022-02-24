'''
https://www.acmicpc.net/problem/2504
() = 2
[] = 3
(x) = 2*x
[x] = 3*x
(xy) = (x)+(y)
'''

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

brakets = input().rstrip()
stack = []
for i in range(len(brakets)):
    flag = True
    if brakets[i] == '(' or brakets[i] == '[':
        stack.append(brakets[i])
    elif brakets[i] == ')' and stack:
        if stack[-1] == '(':
            stack.pop()
            stack.append('2')
        elif stack[-1] == '[':
            flag=False
        elif stack[-1].isdigit():
            sum = 0
            while stack:
                if stack[-1].isdigit():
                    sum += int(stack.pop())
                elif stack[-1] == '(':
                    stack.pop()
                    sum *=2
                    stack.append(str(sum))
                    break
                elif stack[-1] == '[':
                    flag = False
                    break
    elif brakets[i] == ']' and stack:
        if stack[-1] == '[':
            stack.pop()
            stack.append('3')
        elif stack[-1] == '(':
            flag = False
        elif stack[-1].isdigit():
            sum = 0
            while stack:
                if stack[-1].isdigit():
                    sum+= int(stack.pop())
                elif stack[-1] == '[':
                    stack.pop()
                    sum *=3
                    stack.append(str(sum))
                    break
                elif stack[-1] == '(':
                    flag = False
                    break
    else:
        flag = False
    if flag == False:
        print(0)
        break
    print(stack)
if flag == True:
    try:
        nums = list(map(int,stack))
    except:
        print(0)
    else:
        result = 0
        for num in nums:
            result += num
        print(result)

