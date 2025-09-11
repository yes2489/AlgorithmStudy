import sys
import bisect
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))
    
    cnt = 0
    
    for i in a:
        cnt += bisect.bisect_left(b, i)
        
    print(cnt)