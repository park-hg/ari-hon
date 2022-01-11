n = 6
dims = [(30, 35), (35, 15), (15, 5), (5, 10), (10, 20), (20, 25)]

dp = [[-1]* n for _ in range(n)]

for len in range(n):
    for i in range(n-len):
        j = len + i
        if i == j:
            dp[i][j] = 0
        else:
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+dims[i][0]*dims[k][1]*dims[j][1])

print(dp[0][n-1])