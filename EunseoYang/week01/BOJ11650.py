import sys

N=int(sys.stdin.readline())
arr=[]
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr.append([a, b])
arr.sort()
for x,y in arr:
    # 리스트 [x, y]의 각 요소를 변수에 하나씩 언패킹해서 할당
    print(x, y)