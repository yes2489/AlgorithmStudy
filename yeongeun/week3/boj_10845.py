from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
que = deque()

for _ in range(n):
    command = input().strip()

    if command.startswith('push'):
        _, num = command.split()
        que.append(int(num))

    elif command == 'pop':
        if que:
            print(que[0])
            que.popleft()
        else:
            print(-1)

    elif command == 'size':
        print(len(que))

    elif command == 'empty':
        if que:
            print(0)
        else:
            print(1)

    elif command == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
            
    elif command == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)
