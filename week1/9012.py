T = int(input())

vps = []

for x in range(T):
    stack = []
    vps = input()

    for y in vps:
        if y == '(':
            stack.append(x)
        elif y == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                print("NO")
                break

    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')