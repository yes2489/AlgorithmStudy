# 회의실 배정
import sys
input = sys.stdin.readline

N = int(input().strip())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

# 끝나는 시간 기준 오름차순, 끝나는 시간이 같으면 시작 시간 기준 오름차순
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0    # 현재까지 선택된 회의의 끝나는 시간

for start, end in meetings:
    if start >= end_time:
        count += 1
        end_time = end

print(count)
