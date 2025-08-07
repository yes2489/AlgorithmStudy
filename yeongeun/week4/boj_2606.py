import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)

N = int(input()) # 컴퓨터의 수
M = int(input()) # 컴퓨터 쌍의 수

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

dfs(1)

# 1번 컴퓨터를 제외한 감염된 컴퓨터 수 출력
print(sum(visited) - 1)
