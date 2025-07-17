import sys
input = sys.stdin.readline
N = int(input())

point = [list(map(int, input().split())) for _ in range(N)]

point = sorted(point)
#point.sort(key=lambda x: (x[0], x[1]))
for i in range(N):
    print(*point[i])

