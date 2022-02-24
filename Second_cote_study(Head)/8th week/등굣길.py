def solution(m, n,puddles):
    CANT_GO = -int(1e10)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1] = 1
    for pu in puddles:
        c, r =pu
        dp[r][c] = CANT_GO
    for i in range(1,n+1):
        for j in range(1,m+1):
            if dp[i][j] == CANT_GO:
                continue
            if dp[i][j-1] != CANT_GO and dp[i-1][j] ==CANT_GO:
                dp[i][j] = dp[i][j-1]
            elif dp[i][j-1] == CANT_GO and dp[i-1][j] != CANT_GO:
                dp[i][j] = dp[i-1][j]
            elif dp[i][j-1] == CANT_GO and dp[i-1][j] == CANT_GO:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i][j] , dp[i][j-1] + dp[i-1][j])
    return dp[n][m] %1_000_000_007