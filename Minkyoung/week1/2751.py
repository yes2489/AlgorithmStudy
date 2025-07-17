import sys
input = sys.stdin.readline

n = int(input())
list = list(int(input(),) for _ in range(n))
list.sort()
for i in range(n):
    print(list[i])
