import sys
input = sys.stdin.readline

n = int(input())
list = list(map(int, input().split()))
max_num = max(list)
sum = 0
for i in range(n):
    sum += list[i]/max_num*100
print(round((sum / n), 2))