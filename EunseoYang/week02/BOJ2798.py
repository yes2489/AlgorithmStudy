# N장의 카드를 바닥에 놓음
# 외친 M을 넘지 않으면서 M과 최대한 가깝게 (3장)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
card = list(map(int, input().split()))

# 3장의 합이 M을 넘지 않으면서 M과 최대한 가까우면 출력
max_total=0
for i in range(len(card)):
    for j in range(i+1, len(card)):
        for k in range(j+1, len(card)):
            total = card[i]+card[j]+card[k];
            if total <= M:
                max_total = max(max_total, total)
print(max_total)
