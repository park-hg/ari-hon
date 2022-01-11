'''
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A&lang=ja
'''

import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, sys.stdin.readline().split())

edges = []
for _ in range(m):
    edges.append(tuple(map(int, sys.stdin.readline().split())))

parent = list(range(n))
rank = [0] * n

def find(x):
    if parent[x] == x:
        return x
    else:
        return find(parent[x])

def unite(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    else:
        if rank[x] < rank[y]:
            parent[x] = y
        else:
            parent[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

def same(x, y):
    return find(x) == find(y)

def kruskal():
    edges.sort(key=lambda edge: edge[2])
    res = 0
    for s, t, w in edges:
        if not same(s, t):
            unite(s, t)
            res += w
    
    return res

print(kruskal())