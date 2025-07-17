## 11650.py

n = int(input())

array = []

for i in range(n):
    [a,b] = map(int, input().split())
    array.append([a, b])

array.sort()

for i in range(n):
    print(array[i][0], array[i][1])
