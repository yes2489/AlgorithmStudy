from collections import deque

def bfs(start, end):
    queue = deque([start])
    visited = [[0] * l for _ in range(l)]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2] #1시방향부터 시계방향으로 8방향
    dx = [1, 2, 2, 1, -1, -2, -2, -1]

    while queue:
        y, x = queue.popleft()
        if (y, x) == end:
            return visited[y][x]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))


T = int(input())
for _ in range(T):
    l = int(input())
    start = tuple(map(int, input().split())) #deque에서 쓰려고 튜플
    end = tuple(map(int, input().split()))
    ans = bfs(start, end)
    print(ans)

# cnt를 사용하면 단순히 queue에 좌표를 넣을때마다 +1을 한다
# 단순히 방문할때마다 숫자를 추가하는 cnt와 달리
# visited[][] 에 +를 하면 실제 이동 거리를 누적하는 방식이다.
# 기존 cnt 방식으로는 최단거리인지 보장된 값을 받을 수 없다
# 왜냐하면 cnt는 단순히 방문하면, 즉 큐에 들어가면 +1을 하기 때문이다.
# 가령 3번만에 가는경로가 있고 4번만에 가는 경로가 있다면 3번만에 이미 visited = true가 됐기 때문에 4번째 방문때는 조건문에서 걸러진다
# def bfs(start, end):
#     queue = deque([start])
#     visited = [[False] * l for _ in range(l)]
#     dy = [-2, -1, 1, 2, 2, 1, -1, -2] #1시방향부터 시계방향으로 8방향
#     dx = [1, 2, 2, 1, -1, -2, -2, -1]
#     cnt = 0
#     while queue:
#         y, x = queue.popleft()
#         if (y, x) == end:
#             return cnt
#         for i in range(8):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < l and 0 <= ny < l and not visited[ny][nx]:
#                 cnt += 1
#                 visited[ny][nx] = True
#                 queue.append((ny, nx))
#
#
#
# l = int(input())
# start = tuple(map(int, input().split())) #deque에서 쓰려고 튜플
# end = tuple(map(int, input().split()))
#
#
# ans = bfs(start, end)
# print(ans)