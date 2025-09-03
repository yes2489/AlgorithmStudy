# 폰켓몬
def solution(nums):
    type_num = len(set(nums))
    max_num = len(nums) // 2
    return min(type_num, max_num)