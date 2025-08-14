import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    visited[y][x] = True
    if s_list[y][x] == '-':
        nx = x + 1
        if nx < m and not visited[y][nx] and s_list[y][nx] == '-':
            dfs(nx, y)
    elif s_list[y][x] == '|':
        ny = y + 1
        if ny < n and not visited[ny][x] and s_list[ny][x] == '|':
            dfs(x, ny)

n, m = map(int, input().split())
s_list = list()
visited = [[False] * (m+1) for _ in range(n+1)]
count = 0

for _ in range(n):
    s_list.append(list(input()))


for y in range(n):
    for x in range(m):
        if not visited[y][x]:
            count += 1
            dfs(x, y)


print(count)