# N = int(input())
#
# S = list(map(int, input().split()))
#
# max_S = max(S)
# max_idx = []
# for i in range(len(S)):
#     if S[i] == max_S:
#         max_idx.append(i)
# cnt = [1] * len(max_idx)
# for i in range(len(max_idx)):
#     for j in range(1, max_idx[i]+1):
#         if S[j] > S[j-1]:
#             cnt[i] += 1
#     for k in range(max_idx[i], len(S)):
#         if S[k-1] > S[k]:
#             cnt[i] += 1
#
# print(max(cnt))

N = int(input())
S = list(map(int, input().split()))

# 부분수열이 최대가 되는 지점 i를 찾기 위해 반복문을 돌리자

LS = [1] * N
for i in range(N):
    for j in range(i): # 바로 옆에 딱 붙어서 수열이 측정되지 않을 수 있기 때문에
        if S[j] < S[i]: #i, i-1로 비교하는게 아니라 이렇게 i, j로 2중 for문을 한다
            LS[i] = max(LS[i], LS[j] + 1)

RS = [1] * N
for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if S[j] < S[i]:  # i를 봉우리로 보고 오른쪽은 내림차순 → 값이 더 작은 쪽으로 확장
            RS[i] = max(RS[i], RS[j] + 1)

#print(LS)
#print(RS)
# 3) 봉우리 i를 합치기
ans = 0
for i in range(N):
    ans = max(ans, LS[i] + RS[i] - 1)
print(ans)
