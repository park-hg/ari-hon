'''
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C&lang=ja
'''

n, w = 4, 8
product = [(4, 2), (5, 2), (2, 1), (8, 3)]

dp = [[0] * (w+1) for _ in range(n+1)]

for i in range(n):
    value, weight = product[i]
    for j in range(w+1):
        if j < weight:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i+1][j-weight] + value)

print(dp[-1][-1])
