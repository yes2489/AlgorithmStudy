# 의상
from collections import Counter

def solution(clothes):
    clothes_cnt = Counter([category for _, category in clothes])

    answer = 1
    for count in clothes_cnt.values():
        answer *= (count + 1)  # 옷 개수 + 안 입는 경우
    answer -= 1  # 아무것도 안 입는 경우는 제외
    return answer