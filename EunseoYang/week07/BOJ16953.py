import sys
input = sys.stdin.readline

# *= 2
# a = a*10 + 1
a, b = map(int, input().split())

count = 1

while (b >= a):
    if b % 10 == 1:
        b = (b-1) // 10
    elif b % 2 == 0:
        b = b // 2
    else:
        print("-1")
        break
    
    count += 1

    if b == a:
        print(count)
        break
else:
    print("-1")