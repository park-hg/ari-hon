from collections import deque

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(input()))

d = [[float('inf')] * m for _ in range(n)]

que = deque([(0,0)])
d[0][0] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while que: 
    x, y = que.popleft()
    if x == n-1 and y == m-1:
        break
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '0' and d[nx][ny] == float('inf'):
            que.append((nx, ny))
            d[nx][ny] = d[x][y] + 1

print(d[-1][-1])