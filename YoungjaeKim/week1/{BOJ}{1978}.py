import sys
input = sys.stdin.readline
n = int(input())

arr = list(map(int, input().split()))

def is_Prime_Number(x):
    if x < 2:
        return False
    #어떤 수의 int(제곱근)으로 나누어지면 소수가 아니다 -> 최적화
    #ex) 16 -> (2,8) (3,6), (4,4) 이미 2, 3, 4 로 나누어 떨어진게 확인이 되면 곱해야되는 뒤쪽수는 필요없다
    for i in range(2, int(x**0.5) + 1): #소숫점 버림 , +1은 for 문 범위
        if x % i == 0:
            return False
    return True

cnt = 0
for i in arr:
    if is_Prime_Number(i) == True:
        cnt += 1
print(cnt)