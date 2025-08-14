import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

grid = [list(input().strip()) for _ in range(n)]

directions = [(1,0), (-1,0), (0,1), (0,-1)]

visited = [[False]*n for _ in range(n)]

def dfs_R_G_B(x,y):
    visited[y][x] = True
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
            if grid[y][x] == grid[ny][nx]:
                dfs_R_G_B(nx,ny)

def dfs_RG_B(x,y):
    visited[y][x] = True
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
            if grid[y][x] == 'B':
                if grid[y][x] == grid[ny][nx]:
                    dfs_RG_B(nx,ny)
            elif grid[y][x] == 'R' or grid[y][x] == 'G':
                if grid[ny][nx] == 'R' or grid[ny][nx] == 'G':
                    dfs_RG_B(nx, ny)

visited = [[False]*n for _ in range(n)]
x_cnt = 0
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            dfs_R_G_B(x,y)
            x_cnt += 1

visited = [[False]*n for _ in range(n)]
o_cnt = 0
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            dfs_RG_B(x,y)
            o_cnt += 1

print(x_cnt)
print(o_cnt)