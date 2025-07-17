import sys

N=int(sys.stdin.readline())
arr=[int(sys.stdin.readline()) for _ in range(N)]
arr.sort()
# arr 리스트 안의 숫자들을 문자열로 변환 후 `\n` 기준으로 합쳐 한 줄씩 출력
print('\n'.join(map(str, arr)))