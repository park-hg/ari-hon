'''
https://www.acmicpc.net/problem/2098

n = int(input())
W = [list(map(int, input().split())) for _ in range(n)]

'''

n = 4
W = [[0, 10, 15, 20],
     [5, 0, 9, 10],
     [6, 13, 0, 12],
     [8, 8, 9, 0]]

for i in range(n):
    for j in range(n):
        if W[i][j] == 0 and i != j:
            W[i][j] = float('inf')

dp = [[float('inf')]*n for _ in range(1 << n)]

dp[(1>>n)-1][0] = 0
for S in range((1<<n)-2,-1,-1):
    for v in range(n):
        for u in range(n):
            if not (S >> u) & 1:
                dp[S][v] = min(dp[S][v], dp[S|(1<<u)][u]+W[v][u])
#print(dp)


dp2 = [[float('inf')] * (1 << n) for _ in range(n)]

for v in range(n):
    dp2[v][0] = W[v][0]
for v in range(n):
    for S in range(1, (1 << n)):
        for u in range(n):
            if (S >> u) & 1:
                dp2[v][S] = min(dp2[v][S], dp2[u][S-(1<<u)]+W[v][u])
print(dp2)
