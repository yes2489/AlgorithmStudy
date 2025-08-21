# 1535 안녕
import sys
input = sys.stdin.readline

n = int(input().strip())
hp = list(map(int, input().split()))
joy = list(map(int, input().split()))

hp = [0] + hp
joy = [0] + joy

# dp[i][j] = i번째 사람까지 고려했을 때, 체력을 j만큼 썼을 때 얻을 수 있는 최대 기쁨
dp = [[0] * 100 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(100):
        # 인사하지 않는 경우 ( 기쁨은 이전 상태 그대로 유지 )
        dp[i][j] = dp[i-1][j]
        # 인사할 수 있는 경우 ( 체력을 hp[i] 만큼 써야하니까 남은 체력에서 그만큼 빼고, 대신에 joy[i]를 얻는다 )
        if j >= hp[i]:
            dp[i][j] = max(dp[i][j] # i번째 사람에게 인사 안 했을 때
                           , dp[i-1][j - hp[i]] + joy[i] # i번째 사람에게 인사했을 때
                           )

print(dp[n][99])