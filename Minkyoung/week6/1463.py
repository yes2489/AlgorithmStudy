import sys
input = sys.stdin.readline

x = int(input())
dy = [0]*(x+1)
dy[1] = 0

for i in range(2, x+1):
    # -1 하는 경우
    dy[i] = dy[i-1] + 1
    # 2로 나눠지는 경우
    if i % 2 == 0:
        dy[i] = min(dy[i], dy[i//2] + 1)
    # 3으로 나눠지는 경우
    if i % 3 == 0:
        dy[i] = min(dy[i], dy[i//3] + 1)

print(dy[x])
