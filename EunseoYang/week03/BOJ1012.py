import sys
sys.setrecursionlimit(10**6) # 재귀 호출 최대 깊이 설정 함수
input = sys.stdin.readline

# 방향 벡터: 위, 오른쪽, 아래, 왼쪽
DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]

def dfs(r, c):
    # 현재 위치의 배추 방문 처리 (0으로 변경)
    board[r][c] = 0
    
    # 4방향 탐색
    for i in range(4):
        nr = r + DR[i]
        nc = c + DC[i]
        
        # 범위 내에 있고, 연결된 배추가 있다면 재귀적으로 방문
        if (nr >= 0 and nr < n and nc >=0 and nc < m):
                if board[nr][nc] == 1:
                    dfs(nr, nc)

# testcase
t = int(input())
for _ in range(t):
    # m: 가로(열), n: 세로(행), k: 배추가 심어진 위치 개수
    m, n, k = map(int, input().split())
    
    # 배추밭 초기화(0: 배추 없음, 1: 배추 있음)
    board = [[0 for _ in range(m)] for _ in range(n)]
    
    # x, y = 배추의 위치
    for i in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1
    
    total = 0 # 배추 무더기 수 == 필요한 지렁이 수
    
    # 배추밭 순회 시작
    for r in range(n):
        for c in range(m):
            if board[r][c] == 1:
                # 배추가 발견되면 DFS 시작, 하나의 배추 무더기 발견으로 간주
                dfs(r, c)
                total += 1
    print(total)
