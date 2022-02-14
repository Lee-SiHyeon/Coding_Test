'''
https://www.acmicpc.net/problem/1717
'''
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find_parent(node):
    if node == parents[node]:
        return node
    parents[node] = find_parent(parents[node])
    return parents[node]

def same_parent(a, b):
    parent_a = find_parent(a)    
    parent_b = find_parent(b)
    return parent_a == parent_b

def sum_nodes(a,b):
    parent_a = find_parent(a)
    parent_b = find_parent(b)
    if parent_a != parent_b:
        if parent_a < parent_b:
            parents[parent_b] = parent_a
        else:
            parents[parent_a] = parent_b
    
n, m = list(map(int, input().rstrip().split()))
parents = [i for i in range(n+1)]

for _ in range(m):
    com, a, b = list(map(int, input().rstrip().split()))
    #합집합
    if com == 0:
        sum_nodes(a,b)
    # 부모 같은지 확인, 같으면 YES, 다르면 NO 출력
    elif com == 1:
        if same_parent(a,b):
            print('YES')
        else:
            print('NO')