import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

best_sum = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            total = cards[i] + cards[j] + cards[k]
            if total <= m:
                best_sum = max(best_sum, total)

print(best_sum)