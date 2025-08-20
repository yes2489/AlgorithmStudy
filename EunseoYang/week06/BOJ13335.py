import sys
input = sys.stdin.readline


# 트럭 수 n, 다리 길이 w, 다리 최대 하중 l
n, w, l = map(int, input().split())
trucks = list(map (int, input().split()))

time = 0
bridge = [0] * w
# 다리 위 트럭 무게
current_weight = 0

# 모든 트럭이 다리를 건널 때까지 반복
while trucks:
    time += 1
    
    # 다리 맨 앞 칸의 트럭이 빠져나감
    current = bridge.pop(0)
    current_weight -= current
    
    # 대기 트럭이 존재하면 다리에 올릴지 확인
    if trucks: 
        # 최대 하중 안 넘기면 올리기
        if current_weight + trucks[0] <= l:
            # 트럭 진입
            bridge.append(trucks[0])
            current_weight += trucks[0]
            # 트럭 대기열에서 제거
            trucks.pop(0)
        # 올릴 수 없으면 빈칸 채우기
        else:
            bridge.append(0)

# 마지막 트럭 지나가는 시간 더하기
time += w

print(time)