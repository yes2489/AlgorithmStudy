import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000) # RecursionError때문에 늘림

n, m = map(int, input().split())
graph = list()
visited = [[False] * m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y):
    visited[y][x] = True
    area = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= m or ny >= n or nx < 0 or ny < 0: #예외 처리
            continue
        if graph[ny][nx] and not visited[ny][nx]:
            area += 1
            area += dfs(nx, ny)

    return area

for _ in range(n):
    graph.append(list(map(int, input().split())))

area_list = [0]
count = 0
for y in range(n):
    for x in range(m):
        if not visited[y][x] and graph[y][x]:
            area_list.append(dfs(x, y) + 1)
            count += 1

print(count)
print(max(area_list))

