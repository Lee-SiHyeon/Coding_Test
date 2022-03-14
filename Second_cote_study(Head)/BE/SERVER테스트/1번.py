'''
단위당 생산단가가 가장 낮은걸로 그리디 풀이 
'''

def solution(money, costs):
    coins = [1,5,10,50,100,500]
    cost_per_coin = []
    for i, cost in enumerate(costs):
        cost_per_coin.append([i, cost/coins[i]])
    
    cost_per_coin.sort(key = lambda x : x[1])
    
    answer = 0
    for idx, _ in cost_per_coin:
        cnt = money // coins[idx]
        money = money - coins[idx]*cnt
        answer += costs[idx]*cnt

    return answer





def main():
    money =4578
    costs = [1, 4, 99, 35, 50, 1000]
    print(solution(money, costs))

main()