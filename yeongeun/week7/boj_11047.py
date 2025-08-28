# 동전 0
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

ans = 0
# 큰 동전부터 처리
for coin in reversed(coins):
    if K == 0:
        break
    cnt = K // coin        # 이 동전으로 최대 몇 개 쓸 수 있는지
    ans += cnt
    K -= cnt * coin        # 남은 금액 갱신

print(ans)
