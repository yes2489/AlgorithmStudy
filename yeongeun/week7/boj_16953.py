# A -> B
import sys
input = sys.stdin.readline

def solution(a, b):
    answer = 0
    while b > a:
        if b % 10 == 1: # 뒤에 1 붙인 경우
            b //= 10
            answer += 1
            continue
        if b % 2 == 0:  # 2 곱한 경우
            b //= 2
            answer += 1
            continue
        break           # 그 외엔 불가능

    if a != b:
        return -1
    return answer + 1   # 연산 횟수 + 1

A, B = map(int, input().split())
print(solution(A, B))
