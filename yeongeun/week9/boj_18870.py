import sys
input = sys.stdin.readline

n = int(input())
coord = list(map(int, input().split()))

coord_set = sorted(set(coord))

def bisect_left(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

answer = [str(bisect_left(coord_set, p)) for p in coord]
print(' '.join(answer))