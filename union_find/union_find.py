'''
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A&lang=ja
'''
import sys

sys.stdin = open("input.txt", "r")

n, q = map(int, sys.stdin.readline().split())

parent = list(range(n))
rank = [0] * n

def find(x):
    if parent[x] == x:
        return x
    else:
        return find(parent[x])

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


def same(x, y):
    if find(x) == find(y):
        return 1
    else:
        return 0

for _ in range(q):
    com, x, y = map(int, sys.stdin.readline().split())
    if com == 0:
        union(x, y)
    else:
        print(same(x, y))