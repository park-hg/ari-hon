'''
https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_11_B
'''
from collections import defaultdict

'''
n = int(input())
graph = defaultdict(list)
for _ in range(n):
    a = list(map(int, input().split()))
    graph[a[0]].extend(a[1:])
'''
n = 6
graph = {
    1: [2, 2, 3],
    2: [2, 3, 4],
    3: [1, 5],
    4: [1, 6],
    5: [1, 6],
    6: [0]
}

d = [1] * (len(graph))
f = [1] * (len(graph))

dis = [1]
sta = [1]
time = 1

while sta:
    v = sta[-1]
    k = graph[v][0]
    if k == 0:
        sta.pop()
        time += 1
        f[v-1] = time
    else:
        graph[v][0] -= 1
        w = graph[v].pop(1)
        if w not in dis:
            sta.append(w)
            dis.append(w)
            time += 1
            d[w-1] = time

for i in range(n):
    print(i+1, d[i], f[i])