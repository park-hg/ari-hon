'''
https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_f
'''

import heapq
import collections

def dijkstra(a, b):
    distance = [float('inf')] * n
    distance[a] = 0

    heap = [(distance[a], a)]
    while heap:
        current_cost, v = heapq.heappop(heap)
        if distance[v] < current_cost:
            continue
        for w in cost[v]:
            if distance[w] < current_cost + cost[v][w]:
                continue
            else:
                distance[w] = current_cost + cost[v][w]
                heapq.heappush(heap, (distance[w], w))

    if distance[b] == float('inf'):
        return -1
    else:
        return distance[b]

n, k = map(int, input().split())
cost = collections.defaultdict(dict)


for _ in range(k):
    query = list(map(int, input().split()))
    if query[0] == 0:
        a, b = query[1]-1, query[2]-1
        print(dijkstra(a, b))
    else:
        a, b, new_cost = query[1]-1, query[2]-1, query[3]
        if b in cost[a]:
            cost[a][b] = min(cost[a][b], new_cost)
            cost[b][a] = min(cost[b][a], new_cost)
        else:       
            cost[a][b] = new_cost
            cost[b][a] = new_cost