'''
https://atcoder.jp/contests/abc138/tasks/abc138_d
'''
import sys

sys.setrecursionlimit(1000000)

from collections import defaultdict

n, q = map(int, input().split())
graph = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 왜지?
    graph[b].append(a)

count = [0] * n
for _ in range(q):
    p, x = map(int, input().split())
    count[p-1] += x


ans = [0] * n
visited = [False] * n
def dfs(v):
    visited[v-1] = True
    for w in graph[v]:
        if not visited[w-1]:
            count[w-1] += count[v-1]
            dfs(w)

dfs(1)
print(*count)