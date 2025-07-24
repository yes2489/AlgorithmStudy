#10828(스택) : 파이썬은 스택을 따로 제공 X
import sys
input = sys.stdin.readline

n = int(input())
stack = list()
result = list()
for i in range(n):
    go = input()
    if go[:2] == 'pu':
        stack.append(go[5:-1])
    elif go[:2] == 'to':
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[len(stack)-1])
    elif go[:2] == 'si':
        result.append(len(stack))
    elif go[:2] == 'po':
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack.pop())
    elif go[:2] == 'em':
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)

for r in result:
    print(r)
    