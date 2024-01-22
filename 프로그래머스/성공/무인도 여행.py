def solution(maps):
    from collections import deque
    
    h = len(maps)
    w = len(maps[0])
    
    matrix = [list(s) for s in maps]
    
    answer = []
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    def bfs(y, x):
        count = int(matrix[y][x])
        matrix[y][x] = "X"
        deq = deque([[y, x]])
        
        while deq:
            y, x = deq.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<= nx < w and 0<= ny < h:
                    if matrix[ny][nx] != "X":
                        count += int(matrix[ny][nx])
                        matrix[ny][nx] = "X"
                        deq.append([ny, nx])
        return count
    
    for i in range(h):
        for j in range(w):
            if matrix[i][j] != "X":
                answer.append(bfs(i, j))
                
    if answer:
        answer.sort()
    else:
        answer = [-1]

    return answer