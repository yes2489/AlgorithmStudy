# 너무 JAVA같아서ㅠ 파이썬 문법으로 수정...하기...
from itertools import combinations

N, M = map(int, input().split())
card = list(map(int, input().split()))

# combinations: 조합을 자동으로 만들어주는 함수
# combinations(card, 3) => card list에서 3장씩 뽑는 모든 조합
max_total = 0
for combo in combinations(card, 3):
    total = sum(combo)
    if total <= M:
        max_total = max(max_total, total)

print(max_total)