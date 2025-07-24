N, X = map(int, input().split())

arr = list(map(int, input().split()))

prefix = [0 for _ in range(N+1)]

for i in range(N+1):
    prefix.append(arr[i])