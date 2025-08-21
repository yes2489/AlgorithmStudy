import sys

input = sys.stdin.readline

def dfs(x ,y):
    visited[y][x] = True

    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < M and 0 <= ny < N:
            if field[ny][nx] == 1 and not visited[y][x]:
                dfs(nx, ny)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    field = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    worm_count = 0

    for y in range(N):
        for x in range(M):
            if field[y][x] == 1 and not visited[y][x]:
                dfs(x, y)
                worm_count += 1

    print(worm_count)



