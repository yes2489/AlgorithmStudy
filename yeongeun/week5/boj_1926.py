import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split()) # n - 도화지의 세로 크기, m - 도화지의 가로 크기

painting = [list(map(int, input().split())) for _ in range(n)]

directions = [(1,0), (-1,0), (0,1), (0,-1)]

visited = [[False]*m for _ in range(n)]

def dfs(x,y):
    visited[y][x] = True
    width = 1
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
            if painting[ny][nx] == 1:
                width += dfs(nx,ny)
    return width

p_cnt = 0
max_width = 0

for y in range(n):
    for x in range(m):
        if painting[y][x] == 1 and not visited[y][x]:
            size = dfs(x,y)
            p_cnt += 1
            if size > max_width:
                max_width = size

print(p_cnt)
print(max_width)