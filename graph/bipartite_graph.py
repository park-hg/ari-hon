'''
https://leetcode.com/problems/is-graph-bipartite/
'''

graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
n = len(graph)

def dfs(start_v):
    color = [-1] * n
    color[start_v] = 1
    stack = [start_v]
    while stack:
        v = stack.pop()
        for w in graph[v]:
            if color[w] == -1:
                color[w] = 1 - color[v]
                stack.append(w)
            elif color[w] == color[v]:
                return False
    return True

ans = True
for i in range(n):
    ans *= dfs(i)

print(ans)