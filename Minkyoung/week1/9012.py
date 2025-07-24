import sys
input = sys.stdin.readline

n = int(input())
result = []

for i in range(n):
    string = input().rstrip()
    count = 0
    for s in string:
        if s == "(":
            count += 1
        else:
            count -= 1

        if count < 0:
            result.append("NO")
            break
    else:
        if count == 0:
            result.append("YES")
        else:
            result.append("NO")

for r in result:
    print(r)