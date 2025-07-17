import sys
input = sys.stdin.readline

n = int(input())

numbers = []

for _ in range(n):
    num = int(input().rstrip())
    numbers.append(num)

numbers.sort()

for num in numbers:
    print(num)
