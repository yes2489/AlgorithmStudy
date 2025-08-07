from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    directions = [(1,0), (-1,0), (0,1), (0,-1)] # 동서남북
    
    queue = deque()
    queue.append((0,0)) # 시작점
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    
    # 도착지에 도달했으면 그 값이 최단거리
    if maps[n-1][m-1] != 1:
        return maps[n-1][m-1]
    else:
        return -1