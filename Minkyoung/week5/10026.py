import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
# 적록 색약 : 빨강-초록, 파랑

num = int(input())
paint = [list(input()) for _ in range(num)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def n_dfs(x,y):
    visited[y][x] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= num or ny >= num:
            continue
        if not visited[ny][nx] and paint[y][x] == paint[ny][nx]:
            n_dfs(nx, ny)

def y_dfs(x,y):
    visited[y][x] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= num or ny >= num:
            continue
        if not visited[ny][nx] and (paint[ny][nx] == 'R' or paint[ny][nx] == 'G') and (paint[y][x] == 'R' or paint[y][x] == 'G'):
            y_dfs(nx,ny)
        elif not visited[ny][nx] and paint[y][x] == paint[ny][nx] == 'B':
            y_dfs(nx,ny)

visited = [[False] * num for _ in range(num)]
no = 0 #적록 색약 X
for y in range(num):
    for x in range(num):
        if not visited[y][x]:
            no += 1
            n_dfs(x,y)

visited = [[False] * num for _ in range(num)]
yes = 0 #적록 색약 O
for y in range(num):
    for x in range(num):
        if not visited[y][x]:
            yes += 1
            y_dfs(x,y)

print(no, yes)
