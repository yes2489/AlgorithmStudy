import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
board = [list(map(str, input().strip())) for _ in range(n)] # 입력 끝
mixed_board = [row[:] for row in board]

for i in range(n):
    for j in range(n):
        if mixed_board[i][j] == 'G':
            mixed_board[i][j] = 'R'

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c, color):
    # 방문체크
    board[r][c] = 'x'

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == color:
            dfs(nr, nc, color)

def mixed_dfs(r, c, color):
    mixed_board[r][c] = 'x'

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < n and 0 <= nc < n and mixed_board[nr][nc] == color:
            mixed_dfs(nr, nc, color)

cnt = 0
mixed_cnt = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 'R':
            cnt += 1
            dfs(i, j, 'R')
        elif board[i][j] == 'G':
            cnt += 1
            dfs(i, j, 'G')
        elif board[i][j] == 'B':
            cnt += 1
            dfs(i, j, 'B')

for i in range(n):
    for j in range(n):
        if mixed_board[i][j] == 'R':
            mixed_cnt += 1
            mixed_dfs(i, j, 'R')
        elif mixed_board[i][j] == 'B':
            mixed_cnt += 1
            mixed_dfs(i, j, 'B')

print(cnt, mixed_cnt)