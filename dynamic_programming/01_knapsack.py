n, w = 4, 5
product = [(4, 2), (5, 2), (2, 1), (8, 3)]

# top down
def dp1():
    dp = [[0] * (w+1) for _ in range(n+1)]

    for i in range(n):
        value, weight = product[i]
        for j in range(w+1):
            if weight > j:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-weight]+value)

    return dp[-1][-1]

# bottom up
def dp2():
    dp = [[0] * (w+1) for _ in range(n+1)]

    for i in range(n-1, -1, -1):
        value, weight = product[i]
        for j in range(w+1):
            if weight > j:
                dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-weight]+value)
    
    return dp[0][w]