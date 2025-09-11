import sys
input = sys.stdin.readline

m, n = map(int, input().split())
snacks = list(map(int, input().split()))

def is_possible(length):
    return sum(s // length for s in snacks) >= m

lo, hi = 1, max(snacks)
answer = 0

while lo <= hi:
    mid = (lo + hi) // 2
    if is_possible(mid):
        lo = mid + 1
        answer = mid
    else:
        hi = mid - 1

print(answer)