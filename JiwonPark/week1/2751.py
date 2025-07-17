## 2751.py

n = int(input())

array = []

for i in range(n):
    num = int(input())
    array.append(num)

for i in sorted(array):
    print(i)