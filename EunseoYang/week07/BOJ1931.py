import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    time = tuple(map(int, input().split()))
    arr.append(time)

# 끝나는 시간 기준으로 오름차순 정렬
# 끝나는 시간이 같으면 시작하는 시간 기준 오름차순 정렬
arr.sort(key = lambda x:(x[1],x[0]))

last_end = 0
count = 0
for start, end in arr:
    # 회의 시작 시간이 직전 회의가 끝난 시간보다 크거나 같으면
    if  start>= last_end:
        # 회의 진행함
        count += 1
        # 끝나는 시간으로 설정
        last_end = end
        
print(count)