# 시간초과
def solution(n, times):
    # 각 심사관이 언제 끝나는지 기록
    end_times = [t for t in times]
    cnt = 0
    last_time = 0

    while cnt < n:
        # 가장 빨리 끝나는 심사관
        min_time = min(end_times)
        idx = end_times.index(min_time)

        # 한 명 심사 완료
        cnt += 1
        last_time = min_time

        end_times[idx] += times[idx]

    return last_time
