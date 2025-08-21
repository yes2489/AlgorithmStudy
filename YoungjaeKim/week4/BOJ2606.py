from collections import deque
import sys
input = sys.stdin.readline
n = int(input()) #컴퓨터의 수
m = int(input()) # 쌍의 수
start = 1
graph = [[] for _ in range(n+1)]
edges = [list(map(int, input().split())) for _ in range(m)]

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)


visited = [False] * (n+1) # 방문한 컴퓨터 체크

def bfs(start, visited):
    queue = deque([start])
    visited[start] = True
    result = 0 # 감염된 컴퓨터 수
    while queue:
        v = queue.popleft()
        for i in graph[v]: #그래프를 순환하면서 연결되지 않았다면 알아서 반복분에서 나온다
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                result +=1
    return result

print(bfs(1, visited))