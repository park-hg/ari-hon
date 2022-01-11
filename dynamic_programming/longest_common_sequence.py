'''
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C&lang=ja
'''
x = 'abcbdab'
y = 'bdcaba'

dp = [[0] * (len(y)+1) for _ in range(len(x)+1)]

for i in range(len(x)):
    for j in range(len(y)):
        if x[i] == y[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
print(dp)