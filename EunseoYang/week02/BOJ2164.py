from collections import deque
import sys

input = sys.stdin.readline

num = int(input())

# cardList = []
# q = deque(cardList)
# for i in range(1, num+1):
#     q.append(i)

# 바로 deque로 받기
q = deque(range(1, num+1))

# 카드 한 장 남을 때까지 반복
while(len(q) > 1):
    
    # 제일 위의 카드 버리기
    q.popleft()
    
    # 다음 카드 맨 아래로 이동시키기
    q.append(q.popleft())

print(*q)