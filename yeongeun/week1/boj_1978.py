n = int(input())

numbers = list(map(int, input().split()))

cnt = 0

for num in numbers:
    if num < 2:
        continue
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        cnt += 1

print(cnt)
