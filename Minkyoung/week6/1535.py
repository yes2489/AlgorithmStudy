import sys
input = sys.stdin.readline

n = int(input())
result = [0] * 99
ph = list(map(int, input().split()))
feel = list(map(int, input().split()))

for i in range(n-1, 1, -1):
    for j in range(99, 1, -1):
        result[j] = max(feel[i])
                    