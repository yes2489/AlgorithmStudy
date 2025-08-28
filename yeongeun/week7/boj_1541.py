# 잃어버린 괄호
import sys
input = sys.stdin.readline

expr = input().strip()
parts = expr.split('-')

# 각 부분을 '+' 기준으로 나누고 합산
sums = []
for part in parts:
    total = sum(map(int, part.split('+')))
    sums.append(total)

# 첫 부분은 더하고, 이후 부분들은 모두 빼기
result = sums[0]
for num in sums[1:]:
    result -= num

print(result)