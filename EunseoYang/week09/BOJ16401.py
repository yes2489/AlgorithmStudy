import sys
input = sys.stdin.readline

nephew, snack_cnt = map(int, input().split())
snacks = list(map(int, input().split()))

start, end = 1, max(snacks)
ans = 0

while start <= end:
    
    mid = (start + end) // 2
    
    # mid 길이로 잘랐을 때 총 몇 개 나오나 확인
    cnt = 0
    for snack in snacks:
        cnt += snack // mid
    
    if cnt >= nephew:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)