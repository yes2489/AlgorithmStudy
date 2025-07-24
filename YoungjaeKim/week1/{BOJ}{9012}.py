def VPS(lst):
    cnt = 0
    for i in lst:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt < 0: #오른쪽이 더 많아지는 경우 / 오른쪽이 먼저 들어온 경우
            return "NO"
    if cnt == 0:
        return "YES"
    else:
        return "NO"


T = int(input())


for _ in range(T):
    lst = list(input())
    print(VPS(lst))