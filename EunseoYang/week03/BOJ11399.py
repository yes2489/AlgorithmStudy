# 입력받은 대기 시간을 오름차순으로 정렬한 후, 누적합을 구해 총 대기 시간의 합을 최소화
n = int(input())
p = list(map(int, input().split()))
p.sort()

total = 0
current_wait = 0

for i in range(n):
    current_wait += p[i] # 현재 사람까지의 누적 시간
    total += current_wait # 총 합에 더하기
    
print(total)