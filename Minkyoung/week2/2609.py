#최대 공약수, 최소공배수
import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
max_num = max(n,m)
min_num = min(n,m)
for i in range(1, min_num+1):
    if n % i == 0 and m % i ==0:
        a = i

for i in range(1, min_num+1):
    if (max_num * i) % min_num==0:
        b = max_num * i
        break

print(a)
print(b)
