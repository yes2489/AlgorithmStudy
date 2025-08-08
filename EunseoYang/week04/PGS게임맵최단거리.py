from collections import deque

def solution(maps):
    
    # 상하좌우 방향 벡터
    DR = [-1, 0, 1, 0] # 위, 오른쪽, 아래, 왼쪽
    DC = [0, 1, 0, -1]
    
    # 방문 배열 초기화
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    
    # 최단거리: bfs 
    q = deque()
    q.append((0, 0))
    visited[0][0] = True # 시작점 방문 표시
    
    while q:
        r, c = q.popleft() # 현재 위치 꺼내기

        for i in range(4):
            nr = r + DR[i]
            nc = c + DC[i]
            
            # 맵 범위를 벗어나지 않고 아직 방문하지 않은 경우
            if 0 <= nr < len(maps) and 0 <= nc < len(maps[0]) and not visited[nr][nc]:
                visited[nr][nc] = True # 방문 처리
                
                if maps[nr][nc] == 1: # 벽이 아니고 길이라면
                    # 현재 위치까지의 거리 +1 저장
                    maps[nr][nc] = maps[r][c] + 1
                    # 다음 탐색을 위헤 큐에 넣기
                    q.append((nr, nc))
                    
    # 도착 지점이 1이면 도달X -> -1 반환
    # 아니라면 그 위치에 저장된 값이 최단 거리
    return maps[-1][-1] if maps[-1][-1] != 1 else -1
