import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
lst = sorted(lst)
for i in range(N):
    print(lst[i])

# N = int(input())
# lst = [int(input()) for _ in range(N)]
# lst2 = [0 for _ in range(N)]
# #lst[0] = 1
# for i in range(N):
#     lst2[i] = lst[N-1-i]
#
# print(lst2)