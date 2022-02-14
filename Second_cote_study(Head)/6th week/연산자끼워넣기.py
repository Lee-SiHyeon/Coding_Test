'''
https://www.acmicpc.net/problem/14888
'''
import sys
from itertools import permutations
print(sys.stdin)
sys.stdin = open("input.txt")
print(sys.stdin)

input = sys.stdin.readline

N = int(input())
command_map ={
    0 : '+',
    1 : '-',
    2 : '*',
    3 : '//'
}
numbers = list(map(int,input().rstrip().split()))
commands = list(map(int,input().rstrip().split()))
command_list = []
for com, value in enumerate(commands):
    for _ in range(value):
        command_list.append(command_map[com])
sys.stdin = '<stdin>'
print(sys.stdin)
permu_command = list(permutations(command_list))
result_min =1000000000
result_max = -1000000000
for permu in permu_command:
    result = numbers[0]
    for i, per in enumerate(permu):
        if per == "+":
            result += numbers[i+1]
        elif per == "-":
            result -= numbers[i+1]
        elif per == "*":
            result *= numbers[i+1]
        elif per == "//":
            if result < 0:
                result=-((-result) // numbers[i+1])
            else:
                result //= numbers[i+1]
    result_min = min(result_min, result)
    result_max = max(result_max, result)
print(result_max)
print(result_min)

        
    


