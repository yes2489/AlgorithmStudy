import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

# 1) 가로 무늬('-') 세기: 각 행마다 연속된 '-' 구간을 1개로 카운트
h = 0
for r in range(N):
    interval = False  # 현재 행에서 '-' 연속 구간 내부인지 여부
    for c in range(M):
        if board[r][c] == '-':
            # 이전이 '-'가 아니었다면 새로운 구간이 시작됨
            if not interval:
                h += 1
                interval = True
        else:
            # '-' 연속 구간이 끊어짐
            interval = False

# 2) 세로 무늬('|') 세기: 각 열마다 연속된 '|' 구간을 1개로 카운트
v = 0
for c in range(M):
    interval = False  # 현재 열에서 '|' 연속 구간 내부인지 여부
    for r in range(N):
        if board[r][c] == '|':
            if not interval:
                v += 1
                interval = True
        else:
            interval = False

# 총 판자 개수 = 가로 구간 수 + 세로 구간 수
print(h + v)