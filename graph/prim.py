'''
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A&lang=ja
'''

import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, sys.stdin.readline().split())

cost = [[float('inf')] * n for _ in range(n)]
for _ in range(m):
    s, t, w = map(int, sys.stdin.readline().split())
    cost[s][t] = cost[t][s] = w

def prim():
    # 집합X부터 최소 비용
    mincost = [float('inf')] * n
    # 집합X에 포함 되는지
    used = [False] * n

    mincost[0] = 0
    res = 0

    while True:
        v = -1
        for u in range(n):
            if not used[u] and (v == -1 or mincost[u] < mincost[v]):
                v = u
        if v == -1:
            break
        used[v] = True
        res += mincost[v]

        for u in range(n):
            mincost[u] = min(mincost[u], cost[v][u])

    return res