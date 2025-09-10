import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()

left = 1 # 공유기 최소 간격
right = houses[-1] - houses[0] # 공유기 최대 간격
ans = 0

while left <= right:
    mid = (left + right) // 2 # 현재 시도하는 공유기 간격
    cnt = 1 # 첫 번째 집은 무조건 설치
    last = houses[0] # 마지막으로 공유기 설치한 집
    
    for i in range(1, n):
        if houses[i] - last >= mid:
            cnt += 1
            last = houses[i]
    
    if cnt >= c:
        ans = mid
        left = mid + 1 # 공유기 간격 넓히기
    else:
        right = mid - 1 # 공유기 개수 부족으로 간격 줄이기

print(ans)