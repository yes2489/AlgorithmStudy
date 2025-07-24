#1181 단어 정렬
import sys
input = sys.stdin.readline


n = int(input())

words = [str(input()) for i in range(n)]

words = list(set(words))
# words.sort()
# words.sort(key=len)
words.sort(key=lambda x: (len(x), x))

for w in words:
    print(w, end="")
    