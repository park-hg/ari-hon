'''
https://www.acmicpc.net/problem/11657
'''

n, m = 3, 2
#edges = [(1, 2, 4), (1, 3, 3), (2, 3, -4), (3, 1, -2)]
edges = [(1, 2, 4), (1, 2, 3)]

def BellmanFord(edges, source):
    distance = [float('inf')] * n

    distance[source-1] = 0
    for _ in range(n-1):
        for u, v, w in edges:
            if distance[u-1] + w < distance[v-1]:
                distance[v-1] = distance[u-1] + w

    for u, v, w in edges:
        if distance[u-1] + w < distance[v-1]:
            return -1

    return distance

distance = BellmanFord(edges, 1)

if distance == -1:
    print(distance)
else:
    for i in range(1, n):
        if distance[i] == float('inf'):
            print(-1)
        else:
            print(distance[i])