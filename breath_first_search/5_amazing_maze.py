'''
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1166&lang=jp
'''
w, h = 9, 4

left = [[1, 0, 1, 0, 0, 0, 0, 0], 
        [1, 0, 1, 1, 0, 0, 0, 0], 
        [0, 0, 0, 1, 0, 0, 1, 1], 
        [0, 0, 0, 0, 0, 0, 1, 0]]
down = [[0, 1, 1, 0, 1, 1, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 1, 1], 
        [0, 0, 0, 0, 1, 1, 0, 0, 0]]

from collections import deque

grid = [[0] * w for _ in range(h)]
que = deque([(0, 0)])
grid[0][0] = 1

left = [[1] + row for row in left]
down.append([1]*(w-1)+[0])

while que:
    x, y = que.popleft()
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if left[x][y] == 1:
        d.remove((0, -1))
    if down[x][y] == 1:
        d.remove((1, 0))
    if 0 <= y < w-1 and left[x][y+1] == 1:
        d.remove((0, 1))
    if 1 <= x < h and down[x-1][y] == 1:
        d.remove((-1, 0))
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 0:
            grid[nx][ny] = grid[x][y] + 1
            que.append((nx, ny))
print(grid[-1][-1])