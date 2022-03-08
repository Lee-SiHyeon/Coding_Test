def solution(N, number):
    dp = [[] for _ in range(9)]
    for i in range(1,9):
        for j in range(1,i):
            for a in dp[j] :
                for b in dp[i-j]:
                    dp[i].append(a+b)
                    dp[i].append(a-b)
                    if b <=0 :
                        continue
                    else :
                        dp[i].append(a//b)
                    dp[i].append(a*b)
        dp[i].append(int(str(N)*i))
        if number in dp[i]:
            return i 
        dp[i]=list(set(dp[i]))
    return -1