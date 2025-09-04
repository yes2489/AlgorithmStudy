# 전화번호 목록
def solution(phone_book):
    phone_set = set(phone_book)  # 모든 번호를 set에 저장

    for number in phone_set:
        # 길이 1부터 number-1 까지 prefix 확인
        for i in range(1, len(number)):
            if number[:i] in phone_set:
                return False

    return True