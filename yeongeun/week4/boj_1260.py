import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# N - 정점의 개수, M - 간선의 개수, V - 탐색을 시작할 정점의 번호
N, M, V = map(int, input().split())

# 인접리스트로 그래프 구현
graph = [[] for _ in range(N+1)]

# 간선 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    # 양방향 연결
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 것부터 방문할 수 있도록 정렬
for vertexs in graph:
    vertexs.sort()

# DFS 함수
def dfs(vertex):
    visited[vertex] = True
    print(vertex, end=' ')
    for next_vertex in graph[vertex]:
        if not visited[next_vertex]:
            dfs(next_vertex)

# BFS 함수
def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for next_vertex in graph[vertex]:
            if not visited[next_vertex]:
                visited[next_vertex] = True
                queue.append(next_vertex)
    
# DFS 실행
visited = [False] * (N+1)
dfs(V)
print() # 줄바꿈

# BFS 실행
visited = [False] * (N+1)
bfs(V)