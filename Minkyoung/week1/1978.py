import sys
input = sys.stdin.readline

n = int(input())
list = list(map(int, input().split()))
re = 0

for i in range(n):
    status = 1 #1이면 소수
    if list[i] == 1:
        status = 0 #1은 소수X
        continue
    max_num = list[i]

    for j in range(2, max_num):
        if list[i] % j == 0: # 소수 아님
            status = 0
            break

    if status == 1:
        re += 1

print(re)
