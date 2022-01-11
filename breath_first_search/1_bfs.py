'''
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C&lang=ja
'''


from collections import defaultdict

'''
n = int(input())
graph = defaultdict(list)
for _ in range(n):
    u = list(map(int, input().split()))
    graph[u[0]].append(u[1])
'''
n = 4
graph = {
    1: [2, 2, 4],
    2: [1, 4],
    3: [0],
    4: [1, 3]
}

d = [-1] * n

que = [1]
visited = [False] * n
visited[0] = True
d[0] = 0

while que:
    u = que[0]
    k = graph[u][0]
    if k == 0:
        que.pop(0)
    else:
        graph[u][0] -= 1
        v = graph[u].pop(1)
        if not visited[v-1]:
            que.append(v)
            visited[v-1] = True
            d[v-1] = d[u-1] + 1
print(d)