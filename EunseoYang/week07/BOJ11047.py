import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
total = 0

for _ in range(n):
    coin = int(input())
    if coin <= k:
        coins.append(coin)

for i in range(len(coins) -1 , -1, -1):
    if k // coins[i] != 0:
        total += k // coins[i]
        k = k % coins[i]
    if k == 0:
        break

print(total)