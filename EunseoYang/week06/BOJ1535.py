import sys
input = sys.stdin.readline

# dp[j] = 체력 j를 소모했을 때 얻을 수 있는 최대 기쁨
# L[i] = i번째 사람에게 인사할 때 소모되는 체력
# J[i] = i번째 사람에게 인사할 때 얻는 기쁨

n = int(input())
hp = list(map(int, input().split()))
joy = list(map(int, input().split()))

dp = [0] * 100

# 전체 사람 순회
for i in range(n):
    # 체력은 99에서부터 내려옴
    for j in range(99, hp[i]-1, -1):
        # dp[j]는 인사 함 vs 인사하지 않음 중 최대 기쁨
        dp[j] = max(dp[j], dp[j -hp[i]] + joy[i])
        
# 0~99 체력 중 최대 기쁨
print(max(dp))

'''
# 0-1 Knapsack (아이템 한 번만 선택 가능)
# dp[w] = 무게 w일 때 얻을 수 있는 최대 가치

for i in range(n):               # i번째 아이템
    for w in range(W, weight[i]-1, -1):  # 용량 W에서 weight[i]까지 내려옴
        dp[w] = max(dp[w], dp[w - weight[i]] + value[i])

---

# Unbounded Knapsack (아이템을 여러 번 선택 가능)
# dp[w] = 무게 w일 때 얻을 수 있는 최대 가치

for i in range(n):               # i번째 아이템
    for w in range(weight[i], W+1):   # weight[i]부터 W까지 올라감
        dp[w] = max(dp[w], dp[w - weight[i]] + value[i])
        
'''