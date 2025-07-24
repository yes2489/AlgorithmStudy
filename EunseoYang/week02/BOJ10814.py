import sys

input = sys.stdin.readline
# 회원 수 입력
num = int(input())

# 회원 정보 저장할 리스트 초기화
member = []

# 회원 수만큼 반복하면서 나이와 이름을 받아 리스트에 저장
for _ in range(num):
    age, name = input().split()
    member.append([int(age), name])

# member 리스트를 나이 기준으로 정렬
# sorted() 함수의 key를 인자로 lambda 함수 사용 
# -> 각 회원 정보(x)가 [나이, 이름] 형태일 때, x[0](나이)만 추출하여 정렬 기준으로 삼음
# Python의 sorted()는 stable sort로 나이가 같을 경우 입력 순서가 유지 됨
for i in sorted(member, key = lambda x: x[0]):
    print(i[0], i[1])