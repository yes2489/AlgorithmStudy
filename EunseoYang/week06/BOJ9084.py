import sys
input = sys.stdin.readline

# 점화식 아이디어
# dp[j] = 금액 j를 만드는 경우의 수
# 초기값: dp[0] = 1 (아무 동전도 안 쓰는 방법 1가지)
# 갱신: dp[j] += dp[j - coin]  (coin ≤ j)
#       → coin을 하나 쓰고, 나머지 j-coin을 만드는 방법을 더한다
t = int(input()) 

for _ in range(t):
    n = int(input()) # 동전 종류 개수
    lst = list(map(int, input().split())) # 동전 리스트
    k = int(input()) # 목표 금액
    
    # dp[x] = 금액 x를 만드는 경우의 수
    dp = [0] * (k + 1)
    
    # 0원을 만드는 방법은 "아무 동전도 사용하지 않음" 1가지
    dp[0] = 1
    
    # 각 동전 coin에 대해 경우의 수 누적
    for coin in lst:
        # coin 이상 금액부터 갱신
        for j in range(coin, k+1):
            # j원을 만드는 방법 += (j-coin원을 만드는 방법)
            dp[j] += dp[j-coin]
            
    # 목표 금액 k를 만드는 총 경우의 수 출력
    print(dp[k])