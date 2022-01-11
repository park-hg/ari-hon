'''
https://atcoder.jp/contests/abc007/tasks/abc007_3
'''
from collections import deque

'''
r, c = map(int, input().split())
sy, sx = map(int, input().split())
sy, sx = sy-1, sx-1
gy, gx = map(int, input().split())
gy, gx = gy-1, gx-1
grid = []
for _ in range(r):
    grid.append(list(input()))
'''

r, c = 7, 8
sy, sx = 1, 1
gy, gx = 3, 4

grid =[list('########'), list('#......#'), list('#.######'), 
        list('#..#...#'), list('#..##..#'), list('##.....#'), 
        list('########')]

que = deque([(sy, sx)])
grid[sy][sx] = 0

while que:
    x, y = que.popleft()
    if x == gy and y == gx:
        break
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == '.':
            que.append((nx, ny))
            grid[nx][ny] = grid[x][y] + 1

print(grid[gy][gx])