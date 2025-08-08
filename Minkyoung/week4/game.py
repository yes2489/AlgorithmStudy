def solution(maps):
    answer = -1
    temp = 10001
    count = 1
    n = len(maps[0])
    m = len(maps)
    visited = [[False] * n for _ in range(m)]
    def dfs(x, y):
        nonlocal answer, count, temp
        visited[y][x] = True
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        if x == n - 1 and y == m - 1:
            if count < temp:
                temp = count
            return
        
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx == n or ny == m:
                continue
                
            if maps[ny][nx] and visited[ny][nx] == False:
                count += 1
                dfs(nx,ny)
                count -= 1
                visited[ny][nx] = False     
    
    dfs(0, 0)
    
    if temp != 10001:
        answer = temp
        
    return answer
