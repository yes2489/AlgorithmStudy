import sys

input = sys.stdin.readline

# 컴퓨터 수
c = int(input())

# 연결되어있는 컴퓨터 쌍의 수
n = int(input())

# 직접 연결되어 있는 컴퓨터 번호 쌍
board = [[0]*(c+1) for _ in range(c+1)]

# 방문 여부를 저장할 리스트
visited = [False] * (c+1)

# 연결 정보 입력 받기
for _ in range(n):
    x, y = map(int, input().split())
    board[x][y] = board[y][x] = 1

def dfs(now):
    visited[now] = True
    count = 0
    for next in range(1, c+1):
        # 연결 되어있고 아직 방문하지 않은 컴퓨터라면
        if board[now][next] == 1 and not visited[next]:
            count += 1 
            count += dfs(next) # 누적

result = dfs(1)
print(result)