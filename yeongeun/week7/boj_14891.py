import sys
from collections import deque
input = sys.stdin.readline

wheels = [0]
for _ in range(4):
    wheels.append(deque(map(int, input().strip())))

K = int(input())
for _ in range(K):
    num, direction = map(int, input().split())

    rot_dir = [0]*5
    rot_dir[num] = direction

    # 왼쪽 전파
    for i in range(num, 1, -1):
        if wheels[i][6] != wheels[i-1][2]:
            rot_dir[i-1] = -rot_dir[i]
        else:
            break

    # 오른쪽 전파
    for i in range(num, 4):
        if wheels[i][2] != wheels[i+1][6]:
            rot_dir[i+1] = -rot_dir[i]
        else:
            break

    # 회전 적용
    for i in range(1,5):
        if rot_dir[i] != 0:
            wheels[i].rotate(rot_dir[i])

# 결과값 계산
score = sum([wheels[i][0]*(2**(i-1)) for i in range(1, 5)])
print(score)