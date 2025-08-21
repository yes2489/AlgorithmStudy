import sys
input = sys.stdin.readline
from collections import deque

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split())) # 맨 앞 트럭을 뺄 때밖에 없어서 큐로
bridge = [0]*w
count = 0
while len(trucks): # 트럭이 남아있을 때
    bridge.pop(0) # 자동으로 나머지 인덱스 당겨짐
    if sum(bridge) + trucks[0] <= L:
        bridge.append(trucks.popleft())
        count += 1
    else:
        bridge.append(0)
        count += 1    
    
# 마지막 트럭이 다리에 올라갔을 때 반복문 종료하기 때문에
# w만큼 건너 가는 거 따로 더해줌    
print(count + w)
