# push X: add(X)
# pop: pop(), 없을경우 print(-1)
# size: len()
# empty: 비어있으면 1 아니면 0
# top: 가장 위에 있는 정수 없으면 -1
import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    val = list(map(str, input().split()))
    
    match val[0]:
        case 'push':
            stack.append(int(val[1]))
        case 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        case 'size':
            print(len(stack))
        case 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        case 'top':
            if len(stack) == 0:
                print('-1')
            else:
                popItem = stack.pop()
                stack.append(popItem)
                print(popItem)