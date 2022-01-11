'''
https://leetcode.com/problems/number-of-islands/
'''

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
count = 0
def dfs(x, y):
    if grid[x][y] == "1":
        grid[x][y] = "0"
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                dfs(nx, ny)
        return True
    else:
        return 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        count += dfs(i,j)
print(count)
        
        
    