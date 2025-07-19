# 알파벳 소문자로 이루어진 N개의 단어 정렬
# 1. 길이가 짧은 것 부터
# 2. 길이가 같으면 사전 순으로
# 3. 중복제거
import sys
input = sys.stdin.readline

# 입력받기
N = int(input())

# sys.stdin.readline은 개행까지 포함 -> strip으로 개행 제거
words=[input().strip() for _ in range(N)]

# 중복 제거
words = list(set(words))

# 알파벳 순으로 정렬 후 길이 오름차순 정렬
words.sort()
words.sort(key=len)

for word in words:
    print(word)
