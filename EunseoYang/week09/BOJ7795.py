import sys
input = sys.stdin.readline

# b 배열에서 target보다 작은 원소 개수를 이분 탐색으로 반환
def binary_search(b, target):
    left, right = 0, len(b)
    while left < right:
        mid = (left+right) // 2
        if b[mid] < target:
            left = mid+1
        else:
            right = mid
    return left # target보다 작은 원소 개수


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))
    
    cnt = 0
    
    for i in a:
        cnt += binary_search(b, i)
        
    print(cnt)