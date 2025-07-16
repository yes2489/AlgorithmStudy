n = int(input())

for _ in range(n):
    ps = input()
    stack = []

    for ch in ps:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                print('NO')
                break
            stack.pop()
    else:
        if not stack:
            print('YES')
        else:
            print ('NO')
