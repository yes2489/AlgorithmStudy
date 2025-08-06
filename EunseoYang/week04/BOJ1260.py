from collections import deque

# 정점의 개수 n, 간선의 개수 m, 탐색을 시작할 정점의 번호 v
n, m, v = map(int, input().split())

# 인접 행렬 생성 (정점 번호가 1부터 시작하므로 n+1)
dist = [[0]*(n+1) for _ in range(n+1)]
visited = [False] * (n+1) # 방문 배열 초기화

# 간선 정보 입력 (양방향)
for _ in range(m):
    x, y = map(int, input().split())
    dist[x][y] = dist[y][x] = 1

# 깊이 우선 탐색 (DFS)
def dfs(now):
    visited[now] = True # 현재 노드 방문 처리
    print(now, end=" ") # 방문 노드 출력
    
    # 연결된 정점들을 번호 순으로 확인
    for next in range(1, n+1):
        # 인접하고 아직 방문하지 않았다면 재귀 호출
        if dist[now][next] == 1 and not visited[next]:
            dfs(next)
            
dfs(v)
print()

# 너비 우선 탐색 (BFS)
q = deque()
q.append(v)

# BFS용 방문배열 초기화
visited = [False] * (n+1)
visited[v] = True # 시작 정점 방문처리

# 큐가 빌 때까지 반복
while q:
    now = q.popleft()
    print(now, end=" ")
    
    # 현재 정점과 연결된 모든 정점 확인
    for next in range(1, n+1):
        if dist[now][next] == 1 and not visited[next]:
            visited[next] = True
            q.append(next)
