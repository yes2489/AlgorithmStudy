import sys
input = sys.stdin.readline

x = int(input())
 # cnt는 계산 횟수를 저장하는 배열
 # cnt[i] = 정수 i를 1로 만드는 최소 연산 횟수
cnt = [0] * (x + 1)

for i in range(2, x + 1):
    # cnt[1] = 0 (이미 1이므로 연산 0회)
    
    cnt[i] = cnt[i - 1] + 1
    
    if i % 3 == 0:
        cnt[i] = min(cnt[i], cnt[i // 3] + 1)
    if i % 2 == 0:
        cnt[i] = min(cnt[i], cnt[i // 2] + 1)
    
print(cnt[x])