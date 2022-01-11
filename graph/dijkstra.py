edges = [[0, 2, 5, 1, float('inf'), float('inf')],
         [2, 0, 3, 2, float('inf'), float('inf')],
         [5, 3, 0, 3, 1, 5],
         [1, 2, 3, 0, 1, float('inf')],
         [float('inf'), float('inf'), 1, 1, 0, 2],
         [float('inf'), float('inf'), 5, float('inf'), 2, 0]]

n = len(edges)

'''
1. 출발 노드에서 각 노드에 대해 최소값 갱신
2. 갱신한 값 중, 최소값을 가진 노드로 이동--- priority que 이용
3. 미방문 노드에 대해 최소값 갱신
4. 2, 3 반복
'''

def dijkstra(start_v):
    import heapq

    visited = [False] * n
    visited[start_v] = True
    distance = edges[start_v]

    heap = [(distance[start_v], start_v)]
    while heap:
        current_dis, v = heapq.heappop(heap)
        visited[v] = True
        for w in range(n):
            distance[w] = min(distance[w], current_dis + edges[v][w])
            if not visited[w]:
                heapq.heappush(heap, (distance[w], w))
    
    return distance

### visited를 쓸 필요 없다
### edge 를 defaultdict(dict) 로 나타냄으로써 연결되지 않은 노드 탐색 안함

edges2 = {
    0:{1:2, 2:5, 3:1},
    1:{0:2, 2:3, 3:2},
    2:{0:5, 1:3, 3:3, 4:1, 5:5},
    3:{0:1, 1:2, 2:3, 4:1},
    4:{2:1, 3:1, 5:2},
    5:{2:5, 4:2}
}

n = len(edges2)

def dijkstra2(start_v):
    import heapq

    distance = [float('inf')] * n
    distance[start_v] = 0

    heap = [(0, start_v)]
    while heap:
        current_dis, v = heapq.heappop(heap)
        if distance[v] < current_dis:
            continue
        for w in edges2[v]:
            if distance[w] < current_dis + edges2[v][w]:
                continue
            else:
                distance[w] = current_dis + edges2[v][w]
                heapq.heappush(heap, (distance[w], w))
    
    return distance

print(dijkstra2(0))

### 최단경로 찾기

graph = {
    'A': {'B':8, 'C':2, 'D':3},
    'B':{},
    'C':{'B':3, 'D':2},
    'D':{'E':1, 'F':4},
    'E':{},
    'F':{}
}

def dijkstra3(graph, s, t):
    import heapq

    distance = {node:[float('inf'), s] for node in graph}
    distance[s] = [0, s]
    heap = [(distance[s][0], s)]
    while heap:
        current_dis, v = heapq.heappop(heap)
        if distance[v][0] < current_dis:
            continue
        for w in graph[v]:
            if distance[w][0] < current_dis + graph[v][w]:
                continue
            else:
                distance[w] = [current_dis + graph[v][w], v]
                heapq.heappush(heap, (distance[w][0], w))
    path = [t]
    while distance[path[-1]][1] != s:
        path.append(distance[path[-1]][1])
    path.append(s)
    path.reverse()
    print(path)
    return distance

#print(dijkstra3(graph, 'A', 'E'))