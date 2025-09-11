def solution(n, times):
    def is_possible(best_time):
        total = 0
        for t in times:
            total += best_time // t
        return total >= n

    lo, hi = 1, max(times) * n
    answer = hi

    while lo <= hi:
        mid = (lo + hi) // 2
        if is_possible(mid):
            answer = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return answer