N = int(input())
P = list(map(int, input().split()))

P.sort()

waiting_time = 0
total_time = 0

for time in P:
    waiting_time += time
    total_time += waiting_time

print(total_time)