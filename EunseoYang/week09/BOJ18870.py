import sys
input = sys.stdin.readline

# 좌표 압축?
# 정렬 후 중복 제거 -> 인덱스 치환
n = int(input())
arr = list(map(int, input().split()))
sorted_list = sorted(set(arr))

# dict 활용해서 값 -> index 저장
rank = {}
idx = 0
for num in sorted_list:
    rank[num] = idx
    idx += 1

# 원래 배열의 값들을 rank에서 찾아 순위로 변환
res = []
for i in arr:
    res.append(rank[i])

print(*res)