import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    visited[x][y] = True

    if pattern[x][y] == '-':
        ny = y + 1
        if ny < m and not visited[x][ny] and pattern[x][ny] == '-':
            dfs(x, ny)
    elif pattern[x][y] == '|':
        nx = x + 1
        if nx < n and not visited[nx][y] and pattern[nx][y] == '|':
            dfs(nx, y)

n, m = map(int, input().split())
pattern = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

cnt = 0

for x in range(n):
    for y in range(m):
        if not visited[x][y]:
            dfs(x,y)
            cnt += 1

print(cnt)