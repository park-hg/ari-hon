'''
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=ja
'''

n, m = 65, 6
c = [1, 2, 7, 8, 12, 50]

dp = [[float('inf')] * (n+1) for _ in range(m+1)]
dp[0][0] = 0
for i in range(m):
    price = c[i]
    for j in range(n+1):
        if j < price:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = min(dp[i][j], dp[i][j-price] + 1)

print(dp[-1][-1])