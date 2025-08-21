# 11054 가장 긴 바이토닉 부분 수열
import sys
input = sys.stdin.readline

n = int(input().strip())
A = list(map(int, input().split()))

# 증가 부분 수열 계산
increase = [1] * n
for i in range(n):
    for j in range(i):
        if A[j] < A[i]:
            increase[i] = max(increase[i], increase[j] + 1)

# 감소 부분 수열 계산 ( 역방향으로 증가부분 수열 계산 )
decrease = [1] * n
for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if A[j] < A[i]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

# 바이토닉 길이 구하기
answer = 0
for i in range(n):
    answer = max(answer, increase[i] + decrease[i] - 1)

print(answer)
