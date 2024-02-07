def solution(board):
    answer = 0
    
    matrix = [list(i) for i in board]
    
    # R == start, G == end, D == wall
    
    h = len(matrix)
    w = len(matrix[0])
    
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == "R":
                start = [i, j]
            elif matrix[i][j] == "G":
                end = [i,j]
    
    from collections import deque
    
    def bfs(start):
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        
        visited = [[1e9] * w for _ in range(h)]
        visited[start[0]][start[1]] = 1
        
        deq = deque([start])
        
        while deq:
            ny, nx = deq.popleft()
            
            for i in range(4):
                y, x = ny, nx
                
                while 0 <= y + dy[i] < h and 0 <= x + dx[i] < w and matrix[y + dy[i]][x + dx[i]] != "D":
                    y = y + dy[i]
                    x = x + dx[i]

                if visited[ny][nx] + 1 < visited[y][x]:
                    deq.append([y, x])
                    visited[y][x] = visited[ny][nx] + 1

        return visited[end[0]][end[1]]

    answer = bfs(start)
    
    if answer == 1e9:
        answer = -1
    else:
        answer -= 1

    return answer
