'''
https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_e
'''

from collections import deque
from copy import deepcopy
'''
w, h = 8, 4
grid = [[0, 1, 0, 1, 0, 1, 1, 1],
        [0, 1, 1, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 1],
        [0, 1, 1, 0, 1, 0, 1, 0]]
'''

w, h = map(int, input().split())
grid = []
for _ in range(h):
    grid.append(list(map(int, input().split())))


grid = [[0] + row + [0] for row in grid]
grid = [[0] * (w+2)] +  grid + [[0] * (w+2)]
visited = deepcopy(grid)
que = deque([(0, 0)])
visited[0][0] = True


ans = 0
while que:
    x, y = que.popleft()
    if x % 2 == 0:
        dx = [0, -1, -1, 0, 1, 1]
        dy = [1, 0, -1, -1, -1, 0]
    else:
        dx = [0, -1, -1, 0, 1, 1]
        dy = [1, 1, 0, -1, 0, 1]
    for i in range(6):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < h+2 and 0 <= ny < w+2:
            if grid[nx][ny]:
                ans += 1
            if not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx, ny))
print(ans)
