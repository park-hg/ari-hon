p = [(2, 3), (1, 2), (3, 4), (2, 2)]
capacity = 5

dp = [[float('inf')] * (100 * 100 + 1) for _ in range(101)]
dp[0][0] = 0

for i in range(len(p)):
    w, v = p[i]
    for j in range(100 * 100 + 1):
        if v > j:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = min(dp[i][j], dp[i][j - v] + w)

ans = 0
for i in range(100 * 100 + 1):
    if dp[len(p)][i] == capacity:
        ans = i
print(ans)