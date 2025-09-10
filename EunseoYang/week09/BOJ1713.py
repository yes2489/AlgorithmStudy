import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))

# 학생번호, 추천수, 시간 저장 배열
pictures = []

for t, s in enumerate(arr):
    # 이미 사진틀에 있는 경우 → 추천 수 +1
    in_pictures = False
    for i in range(len(pictures)):
        if pictures[i][0] == s:
            num, cnt, time = pictures[i]
            pictures[i] = (num, cnt + 1, time)
            in_pictures = True
            break

    if in_pictures:
        continue

    # 사진틀이 비어 있는 경우
    if len(pictures) < n:
        pictures.append((s, 1, t))
        continue

    # 추천 수 적고 오래된 학생 제거
    pictures.sort(key=lambda x: (x[1], x[2]))
    pictures.pop(0)
    pictures.append((s, 1, t))

nums = []
for p in pictures:
    num = p[0]
    nums.append(num)

ans = sorted(nums)

for x in ans:
    print(x, end=" ")
