# 13335 트럭
from collections import deque

n, w, L = map(int, input().split()) # n - 다리를 건너는 트럭의 수, w - 다리의 길이, L - 다리의 최대 하중
trucks = deque(map(int, input().split()))

bridge = deque([0] * w)

time = 0
while True:
    time += 1
    bridge.popleft()
    if trucks and sum(bridge) + trucks[0] <= L:
        bridge.append(trucks.popleft())
    else:
        bridge.append(0)
    
    if not trucks and sum(bridge) == 0:
        break

print(time)