import sys
input = sys.stdin.readline

t = int(input()) 
re = list()

for _ in range(t):
    n = int(input()) # 동전 가지 수
    coin = list(map(int, input().split()))
    m = int(input())
    dp = [0]*(m+1)
    dp[0] = 1
    for c in coin:
        for j in range(c, m+1):
            dp[j] = dp[j-c] + dp[j]
    re.append(dp[m])

print(*re, sep='\n')
