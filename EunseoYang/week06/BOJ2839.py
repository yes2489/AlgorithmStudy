n = int(input()) # 설탕 무게

# 필요한 설탕 봉지 수
cnt = 0

# n=0인 경우도 통과 케이스
while n >= 0:
    # 5로 나눠지는 순간
    # 지금까지 빼온 3kg 봉지 개수(cnt) + (남은 n // 5) 봉지로 답이 완성
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break
    
    # 5로 안나눠 떨어지면 3kg 봉지 빼고 다시 확인
    n -= 3
    cnt += 1
else:
    # while문이 끝났는데도 답을 못 찾은 경우
    print('-1')