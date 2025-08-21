# 9084 동전
import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    n = int(input().strip())
    coins = list(map(int, input().split()))
    m = int(input().strip())

    dp = [0] * (m+1)
    dp[0] = 1

    for coin in coins:
        for amount in range(coin, m+1):
            dp[amount] += dp[amount - coin]
        
    print(dp[m])
