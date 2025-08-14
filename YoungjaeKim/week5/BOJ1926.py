import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, visited, y, x):
    visited[y][x] = True
    picture = 1 #그림의 넓이 1
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<n and 0<=nx<m and not visited[ny][nx] and graph[ny][nx] == 1:
            picture += dfs(graph, visited, ny, nx)

    return picture

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
max_picture = 0
cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt += 1
            picture = dfs(graph, visited, i, j)
            max_picture = max(picture, max_picture)
            # visited는 dfs에서 수정하면 그게 반복문에도 반영된다 즉 매개변수로 넘긴 변수룰 수정해도 원본 변수 역시 바뀐다.
            # 따라서 이걸 바탕으로 그래프를 탐색하고
            # 실질적인 그림의 누적 크기는 dfs를 바탕으로 탐색한다
            # 각 그림의 영역이 끊어져 있기 때문에
            # dfs한번에 모든걸 탐색할 수 있고
            # 반복문을 통해 끊어진 영역을 넘어가서? 다시 각 영역별로 탐색한다

print(cnt)
print(max_picture)

