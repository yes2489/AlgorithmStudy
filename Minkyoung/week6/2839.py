import sys
input = sys.stdin.readline

# 3 or 5
n = int(input())
# 설탕의 개수가 최대 5000개
dy = [5000]*5001
# 설탕의 개수마다 최소 배달 횟수 기록
# 3개, 5개 일때는 1번씩 배달함, (1,2,4)는 배달할 수 없음
dy[3] = dy[5] = 1

# 6개부터
# 설탕 3개짜리를 추가로 들어서 6이 된건지
# 설탕 5개까지를 추가로 들어서 6이 된건지
# 둘 중에 작은 값을 선택해서 +1
for i in range(6, n+1):
    dy[i] = min(dy[i-3], dy[i-5]) + 1

if dy[n] >= 5000:
    print(-1)
else:
    print(dy[n])
    