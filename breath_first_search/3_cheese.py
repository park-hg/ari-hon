'''
https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_e
'''

from collections import deque
import copy
'''
h, w, n = 4, 5, 2
grid = [list('.X..1'), list('....X'), list('.XX.S'), list('.2.X.')]
'''
h, w, n = map(int, input().split())
grid = []
for _ in range(h):
    grid.append(list(input()))

visited = [[False] * w for _ in range(h)]
dis = [[0] * w for _ in range(h)]


for i in range(h):
    for j in range(w):
        if grid[i][j] == 'S':
            grid[i][j] = '0'
            x_0, y_0 = i, j
        if grid[i][j] == 'X':
            visited[i][j] = True


def bfs(i, sx, sy):
    que = deque([(sx, sy)])
    visited_tmp = copy.deepcopy(visited)
    dis_tmp = copy.deepcopy(dis)
    while que:
        x, y = que.popleft()
        visited_tmp[x][y] = True
        if grid[x][y] == str(i+1):
            break
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for j in range(4):
            nx, ny = x+dx[j], y+dy[j]
            if 0 <= nx < h and 0 <= ny < w and not visited_tmp[nx][ny]:
                que.append((nx, ny))
                visited_tmp[nx][ny] = True
                dis_tmp[nx][ny] = dis_tmp[x][y] + 1
    return dis_tmp[x][y], x, y

ans, x, y = bfs(0, x_0, y_0)
for i in range(1, n):
    time, x, y = bfs(i, x, y)
    ans += time
print(ans)