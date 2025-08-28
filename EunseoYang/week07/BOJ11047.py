import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

coins.sort(reverse=True)

cnt = 0
for coin in coins:
    if k == 0:
        break
    
    cnt += k // coin # 해당 동전 몇 개 쓸 수 있는지 저장
    k %= coin # 남은 금액 갱신

print(cnt)