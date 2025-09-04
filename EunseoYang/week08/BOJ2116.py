import sys
input = sys.stdin.readline

n = int(input())  # 주사위 개수
dice = [list(map(int, input().split())) for _ in range(n)]  # 각 주사위 면 정보

# 주사위에서 마주보는 면을 매핑 (문제에서 주어진 규칙)
opposite = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

answer = 0

# 첫 번째 주사위의 "아래 면"을 어떤 면으로 시작할지 6가지 경우 모두 시도
for bottom in range(6):
    top = opposite[bottom]  # 현재 주사위의 윗면 인덱스
    cnt = 0  # 현재 경우의 합계

    # 첫 번째 주사위의 윗면 값
    top_value = dice[0][top]

    # 첫 번째 주사위의 옆면 중 가장 큰 값 더하기
    # (윗면/아랫면을 제외한 나머지 4개 중 최댓값)
    cnt += max(dice[0][i] for i in range(6) if i not in (bottom, top))

    # 두 번째 주사위부터 마지막 주사위까지 반복
    for i in range(1, n):
        # 현재 주사위에서 아랫면이 이전 주사위 윗면 값과 같아야 함
        bottom = dice[i].index(top_value)
        top = opposite[bottom]  # 현재 주사위의 윗면 인덱스
        top_value = dice[i][top]  # 윗면 값 갱신

        # 옆면 중 최댓값 더하기
        cnt += max(dice[i][j] for j in range(6) if j not in (bottom, top))

    # 최댓값 갱신
    answer = max(answer, cnt)

print(answer)

"""
    1. 주사위의 마주보는 면(0-5, 1-3, 2-4)을 미리 딕셔너리로 저장
    2. 첫 번째 주사위의 아랫면을 6가지 경우 모두 시도
    3. 현재 아랫면이 정해지면 윗면이 자동으로 결정
    4. 아랫면과 윗면을 제외한 4개의 면 중 최댓값을 골라 합산
    5. 다음 주사위로 넘어가면서 이전 주사위의 윗면 값이 현재 주사위 아랫면 값과 일치하도록 맞춤
    6. 이를 모든 경우에 대해 반복해 최대값을 구함
"""