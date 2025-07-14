import sys

N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
maxScore = max(scores)

total = 0
for score in scores:
    total += score/maxScore*100
    
print(total/N)