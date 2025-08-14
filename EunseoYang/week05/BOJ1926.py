import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):
    # (r, c)에서 시작하는 그림의 넓이를 반환
    
    # 현재 위치 방문 처리
    board[r][c] = 0
    area = 1
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # 범위 안에 있고, 아직 방문하지 않은(값이 1인) 칸이라면
        if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 1:
            area += dfs(nr, nc)
    return area

cnt = 0
max_area = 0

# 전체 격자 순회
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            cnt += 1
            max_area = max(dfs(i,j), max_area)
            
print(cnt, max_area, sep='\n')