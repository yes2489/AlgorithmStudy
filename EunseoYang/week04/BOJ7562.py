# 필요한 모듈 임포트 (queue 사용)
import sys
from collections import deque

input = sys.stdin.readline

# 나이트가 이동할 수 있는 8가지 방향 정의
DR = [-2, -1, 1, 2, 2, 1, -1, -2]
DC = [1, 2, 2, 1, -1, -2, -2, -1]

# 테스트 케이스 개수 입력
t = int(input())
for _ in range(t):
    
    # 체스판 크기 입력
    size = int(input())

    # 시작 좌표, 도착 좌표 입력
    start_r, start_c = map(int, input().split())
    end_r, end_c = map(int, input().split())

    # 방문 체크 및 거리 저장용 2차원 배열 초기화
    board = [[0]*size for _ in range(size)]
    visited = [[False] * size for _ in range(size)]

    # 큐 초기화 및 시작 위치 넣기
    q = deque()
    q.append((start_r, start_c))
    visited[start_r][start_c] = True
    
    # BFS 시작
    while q:
        # 현재 위치 꺼내기
        r, c = q.popleft()
        
        # 가지치기
        if (r, c) == (end_r, end_c):
            break
        
        # 8가지 방향 탐색
        for i in range(8):
            nr = r + DR[i]
            nc = c + DC[i]
            
            # 체스판 범위 내이고 아직 방문하지 않은 경우
            if 0 <= nr < size and 0 <= nc < size and not visited[nr][nc]:
                # 방문 표시
                visited[nr][nc] = True
                # 거리 갱신 (이전 칸 + 1) -> board는 지금 칸까지 오는데 걸린 이동 횟수
                board[nr][nc] = board[r][c] + 1
                # 큐에 추가
                q.append((nr, nc))

    # 도착 위치의 거리 출력
    print(board[end_r][end_c])
    