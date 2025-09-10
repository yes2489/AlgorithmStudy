import sys
input = sys.stdin.readline

n, c = map(int, input().split())
points = [int(input()) for _ in range(n)]

points.sort()

def is_possible(distance):
    cnt = 1
    last = points[0]

    for i in range(1, n):
        if points[i] - last >= distance:
            cnt += 1
            last = points[i]
    return cnt >= c

lo, hi = 1, points[-1] - points[0]
answer = 0

while lo <= hi:
    mid = (lo + hi) // 2
    if is_possible(mid):
        answer = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(answer)