import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for j in range(T):
    I = int(input())
    now_dc, now_dr = map(int, input().split())
    target_dc, target_dr = map(int, input().split())

    board = [[0]*I for _ in range(I)]
    
    queue = deque()
    queue.append((now_dc, now_dr))

    directions = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]

    if now_dc == target_dc and now_dr == target_dr:
        print(0)
    else:
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < I and 0 <= ny < I:
                    if board[nx][ny] == 0:
                        board[nx][ny] = board[x][y] + 1
                        queue.append((nx, ny))
    
            if board[target_dc][target_dr] != 0:
                print(board[target_dc][target_dr])
                break