import sys
input = sys.stdin.readline

# '-' 기준으로 분리
init = input().split('-')

res = 0

# 첫 번째 덩어리를 + 기준으로 더한 값을 res에 넣음
first = init[0].split('+')
for num in first:
    res += int(num)

# 나머지 덩어리들을 + 기준으로 더한 후 전부 빼기
for part in init[1:]:
    nums = part.split('+')
    for num in nums:
        res -= int(num)

print(res)