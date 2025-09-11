import sys
input = sys.stdin.readline

n = int(input().rstrip())
total_rec = int(input().rstrip())
rec_l = list(map(int, input().split()))

frames = [] # 원소는 (student, seq, cnt)

for seq, student in enumerate(rec_l):
    for i in range(len(frames)):
        if frames[i][0] == student:
            frames[i] = (frames[i][0], frames[i][1], frames[i][2] + 1)
            break
    else:
        if len(frames) >= n:
            frames.sort(key=lambda x: (x[2], x[1]))
            frames.pop(0)
        frames.append((student, seq, 1))

result = sorted([student for student, _, _ in frames])
print(*result)