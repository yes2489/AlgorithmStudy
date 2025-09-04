from collections import Counter

def solution(clothes):
    counts = Counter(category for _, category in clothes)
    answer = 1
    for _, count in counts.items():
        answer *= (count + 1)
    return answer-1