def solution(nums):
    # 중복 제거된 종류 수
    numbers = list(set(nums))
    # 실제 선택할 수 있는 수랑 비교해서 더 작은 값
    return min(len(numbers), len(nums)//2)