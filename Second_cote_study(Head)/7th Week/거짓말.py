'''
https://www.acmicpc.net/problem/1043
'''
import sys
from collections import deque
input = sys.stdin.readline

N,M = list(map(int,input().rstrip().split()))
true_false = [2] * (N+1)
go_party = [ [] for i in range(N+1)]
query_visit = [False] * (M+1)
truths = list(map(int,input().rstrip().split()))
num = truths[0]

#1. 진실을 아는사람이 없으면 모든 파티에서 가능
if num == 0:
    print(M)
else:
    # 2. 진실을 아는사람들이 있다면, 모든 파티를 일단 queries에 저장합니다.
    queries = []
    for _ in range(M):
        queries.append(list(map(int,input().rstrip().split()))[1:])
    
    # 3.진실을 아는 사람들 목록을 가져와서 true_false에 True로 표기해둡니다.
    truths = truths[1:]
    for truth in truths:
        true_false[truth] = True

    # 4. 모든 쿼리를 돌면서
    for i, query in enumerate(queries):
        # 5. 파티에 진실을 아는 사람이 있는지 확인합니다. (flag)
        flag = False 
        for person in query:
            # 6. 사람이 어느 쿼리에 속하는지 graph를 만들어둡니다.
            go_party[person].append(i)
            if true_false[person] == True:
                flag = True
        
        # 7. 파티에 진실을 아는사람이 있다면, 그사람들과 함께온 사람들을 True로 바꿔줘야합니다.
        if flag == True:
            # 8. 이때 bfs로 어떤 쿼리를 방문해야하는지 bfs로 탐색합니다.
            # 왜냐하면 진실을 모르다가 알게되는 경우, 그 사람이 가는 파티의 사람들을 모두 True로 바꿔줘야합니다.
            query_visit[i] = True
            dq = deque()
            dq.append(i)
            while dq:
                idx = dq.popleft()
                for person in queries[idx]:
                    # 9. 다음 방문해야하는 쿼리를 dq에 저장해둡니다.
                    for queryIdx in go_party[person]:
                        if query_visit[queryIdx] == False:
                            # 중복 방문 방지
                            query_visit[queryIdx] = True
                            dq.append(queryIdx)
                    true_false[person] = True
                
        else:
            # 10. 아무도 진실을 모르는 파티라면 False처리합니다.
            for person in query:
                if true_false[person] ==2:
                    true_false[person] = False
    
    # 11. 모든 파티를 돌면서 진실을 아는 사람이 없는 경우에만 result를 증가시킵니다.
    result = 0
    for query in queries:
        sum = 0
        for person in query:
            if true_false[person] == True:
                sum +=1
        if sum ==0:
            result +=1
    print(result)