import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) #재귀함수 사용시 필수
MAX = 50 + 10

T = int(input())
result = list()

dirx = [1,-1,0,0]
diry = [0,0,1,-1]
def dfs(y, x):
    global visited #필요?
    visited[y][x] = True
    for i in range(4):
        newY = y + diry[i]
        newX = x + dirx[i]
        if graph[newY][newX] and not visited[newY][newX]:
            dfs(newY, newX)

        

for _ in range(T):
    M, N, K = map(int, input().split(' '))
    graph = [[False] * MAX for _ in range(MAX)]
    visited = [[False] * MAX for _ in range(MAX)]
    for _ in range(K):
        x, y = map(int, input().split(' '))
        graph[y + 1][x + 1] = True

    answer = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if graph[i][j] and not visited[i][j]:
                dfs(i, j)
                answer += 1
    result.append(answer)

for r in result:
    print(r)
