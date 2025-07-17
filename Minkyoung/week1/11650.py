import sys
input = sys.stdin.readline

n = int(input())
num = list()
for i in range(n):
    x, y = map(int, input().split(" "))
    num.append((x, y))

num.sort()

for x, y in num:
    print(x, y)
