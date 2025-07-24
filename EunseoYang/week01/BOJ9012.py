tc = int(input())
for _ in range(tc):
    s = input()
    stack = []
    isValid = True
    for char in s:
        # '('일 경우에만 stack에 넣기
        if char == '(':
            stack.append(char)
        else:
            # ')'일 경우 pop으로 꺼낼 수 있으면 정상
            if stack:
                stack.pop()
            else:
                # 없으면 비정상
                isValid = False
                break
    if stack:
        isValid = False
        
    if isValid == True:
        print('YES')
    else:
        print('NO')