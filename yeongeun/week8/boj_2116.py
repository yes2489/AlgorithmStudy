# 주사위 쌓기
import sys

input = sys.stdin.readline

# 주사위 면 대응 (0-5, 1-3, 2-4)
opposite = [5, 3, 4, 1, 2, 0]

n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]

answer = 0

# 첫 번째 주사위의 아랫면을 무엇으로 두는지 6가지 경우 탐색
for bottom_idx in range(6):
    top_val = dices[0][opposite[bottom_idx]]  # 첫 주사위 윗면 값
    sum_val = max([dices[0][i] for i in range(6) if i not in (bottom_idx, opposite[bottom_idx])])

    # 두 번째 주사위부터는 자동 결정
    for j in range(1, n):
        # 이전 주사위의 윗면 값이 이번 주사위의 아랫면 값이 되어야함
        bottom_idx = dices[j].index(top_val)
        top_idx = opposite[bottom_idx]
        top_val = dices[j][top_idx]

        # 이번 주사위의 측면 중 최댓값 더하기
        sum_val += max([dices[j][i] for i in range(6) if i not in (bottom_idx, top_idx)])

    answer = max(answer, sum_val)

print(answer)
