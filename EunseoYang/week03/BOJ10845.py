import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = []
q = deque(q)

for _ in range(n):
    val = list(map(str, input().split()))
    match val[0]:
        case 'push':
            q.append(int(val[1]))
        case 'pop':
            if (len(q) == 0):
                print ('-1')
            else:
                print(q.popleft())
        case 'size':
            print(len(q))
        case 'empty':
            if (len(q) == 0):
                print ('1')
            else:
                print('0')
        case 'front':
            if (len(q) == 0):
                print ('-1')
            else:
                print(q[0])
        case 'back':
            if (len(q) == 0):
                print ('-1')
            else:
                print(q[-1])
