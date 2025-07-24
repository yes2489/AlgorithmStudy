#정답
import sys
input = sys.stdin.readline

def binary_search(target, data):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return True
        elif data[mid] > target:
            end = mid - 1
        elif data[mid] < target:
            start = mid + 1

    return False

n = int(input())
num_list1 = list(map(int, input().split()))
num_list1.sort()

m = int(input())
num_list2 = list(map(int, input().split()))

for i in num_list2:
    if binary_search(i, num_list1):
        print(1)
    else:
        print(0)
        