## 1978.py

n = int(input())
array = list(map(int, input().split()))
count = 0

for x in array:
    if x < 2:
        continue
    prime = True
    for y in range(2, x):
        if x % y == 0:
            prime = False
            break
    if prime:
        count += 1

print(count)