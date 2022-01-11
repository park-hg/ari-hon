'''
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C&lang=ja

https://leetcode.com/problems/course-schedule-iv/submissions/
'''

import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, sys.stdin.readline().split())
dp = [[float('inf')] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    dp[a][b] = c
for i in range(n):
    dp[i][i] = 0

def warshall_floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
    for i in range(n):
        if dp[i][i] < 0:
            return -1
    for i in range(n):
        for j in range(n):
            if dp[i][j] == float('inf'):
                dp[i][j] = 'INF'
    return dp

ans = warshall_floyd()

if ans == -1:
    print('NEGATIVE CYCLE')
else:
    for lst in ans:
        print(*lst)