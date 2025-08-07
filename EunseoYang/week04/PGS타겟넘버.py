def solution(numbers, target):
    answer = 0
    
    # DFS를 재귀함수로 구현
    def dfs(index, current_sum):
        # 모든 숫자를 다 사용한 경우
        if index == len(numbers):
            # 현재 합이 타겟과 같다면 경우의 수 +1
            if current_sum == target:
                # nonlocal: 바로 바깥 함수의 지역 변수
                nonlocal answer
                answer += 1
            return
            
        # 현재 숫자를 더하는 경우
        dfs(index+1, current_sum + numbers[index])
        
        # 현재 숫자를 빼는 경우
        dfs(index+1, current_sum - numbers[index])
    
    # 탐색 시작 (index 0, 현재 합 0부터 시작)
    dfs(0,0)
    
    return answer