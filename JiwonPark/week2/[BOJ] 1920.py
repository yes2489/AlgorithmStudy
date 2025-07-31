import sys

n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
arr1.sort()

m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

for x in arr2:
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if x > arr1[mid]:
            start = mid + 1
        elif x < arr1[mid]:
            end = mid - 1
        else:
            start = mid
            end = mid
            break
    if start == mid and end == mid:
        print(1)
    else:
        print(0)