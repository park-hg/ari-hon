graph = {
    1: [2, 3],
    2: [3, 4],
    3: [5],
    4: [6],
    5: [6],
    6: []
}


def recursive_dfs(v, discovered = []):
    if v not in discovered:
        discovered.append(v)
        for w in graph[v]:
            recursive_dfs(w, discovered)
    return discovered


def recursive_dfs2(v, discovered = []):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            recursive_dfs2(w, discovered)
    return discovered

def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        print(stack)
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in sorted(graph[v], reverse=True):
                stack.append(w)
    return discovered