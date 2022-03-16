'''
https://programmers.co.kr/learn/courses/30/lessons/72413

합승하지 않는경우 따로 구하고, 합승 하는 경우 따로 구해서 
조합을 만들어서 풀어야할것 같은데..?

합승하는 경우 경로의 cost를 절반으로 해서 구해야 하고
S-> 최종 합승 지점 -> A, B의 목적지 까지의 최단경로 
vs
합승 안하는 경우

이거 경우의수 존나 많으니까 플로이드 와샬로 풀자.(dp)
백트래킹으로 풀면 답도없을듯.
플로이드 와샬.. 음
O(V^2)인가 ?
지금 V는 200이고
40000이면 충분하겠네,  오케 레츠기릿
'''



def solution(n, s, a, b, fares):
    # n =지점 갯수 3~200
    # s = start, a,b각자의 목적지
    # fares = n*(n-1)/2 모든 목적지가 다 연결되어 있을 수도 있다.
    INF = int(1e+5)
    # 합승 안하는 경우
    graph_dp = [[INF for _ in range(n+1) ] for _ in range(n+1)] 
    for i in range(1,n+1):
        graph_dp[i][i] = 0
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        start, end, cost = fare
        graph[start].append([end, cost])
        graph[end].append([start, cost])
        graph_dp[start][end] = cost
        graph_dp[end][start] = cost

    #플로이드 와샬
    for k in range(1,n+1):
        for start in range(1,n+1):
            for end in range(1, n+1):
                if graph_dp[start][end] > graph_dp[start][k] + graph_dp[k][end]:
                    graph_dp[start][end] = graph_dp[start][k] + graph_dp[k][end]
    # 이제 어떤 노드에서 출발해도 최단 경로 값을 알 수 있음.
    # 1. 합승 하지 않고 각자 가는 경우
    answer = graph_dp[s][a] + graph_dp[s][b]

    # 2. 합승 하는 경우 
    # k번 노드까지 가고 , 각자 방향으로 가는 경우.
    # 그런데, 그 k번 노드가 A 혹은 B의 도착지점인 경우 생각할 필요 있을듯.
    for k in range(1,n+1):
        # 합승해서 간 위치가 a의 도착지점 인 경우
        if k == a:
            cost = graph_dp[s][k] + graph_dp[k][b]
            
        # 합승해서 간 위치가 a의 도착지점 인 경우
        elif k == b:
            cost = graph_dp[s][k] + graph_dp[k][a]
        else:
            cost = graph_dp[s][k] + graph_dp[k][a] + graph_dp[k][b]
        answer = min(answer , cost)
    return answer


def main():
    n,s,a,b = 6,4,6,2
    fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
    print(solution(n,s,a,b,fares))

main()