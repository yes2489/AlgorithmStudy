import sys
from functools import lru_cache


sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#코딩 테스트에서 lru_cache는 파이썬의 functools 모듈에 포함된 데코레이터로,
# 함수의 결과를 캐싱하여 동일한 입력에 대한 반복적인 계산을 줄여 성능을 향상시키는 데 사용

@lru_cache(maxsize=None) #@cache
def max_hp(idx, hp, happy):
    if idx == N:
        return happy
    ans = max_hp(idx+1, hp, happy) #일단 인사 안했을 때 값을 보관하고
    if hp - L[idx] > 0: # 인사하고나서 hp가 남아있을 때만
        #조건문 통과했으면 인사 했을때랑 안했을 때 중 최대 값을 ans에 갱신
        ans = max(max_hp(idx+1, hp - L[idx], happy+J[idx]), max_hp(idx+1, hp, happy))
    return ans

N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))
hp = 100

print(max_hp(0, hp, 0))
