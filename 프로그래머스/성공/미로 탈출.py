from collections import deque

def solution(maps):
    answer = 0
    
    matrix = [list(i) for i in maps]
    
    # print(matrix)
    
    h = len(matrix)
    w = len(matrix[0])
    
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == "L":
                lever = [i,j]
            elif matrix[i][j] == "S":
                start = [i,j]
            elif matrix[i][j] == "E":
                end = [i,j]
                
    print(start, lever, end)
    
    def bfs(start, graph, target):
        
        deq = deque([start])
                
        visited = [[0] * w for _ in range(h)]
        
        visited[start[0]][start[1]] = 1
        
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        
        while deq:
            y, x = deq.popleft()
        
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < w and 0 <= ny < h:
                    if visited[ny][nx] == 0 and graph[ny][nx] != "X":
                 from collections import deque

def solution(maps):
    answer = 0
    
    matrix = [list(i) for i in maps]
    
    # print(matrix)
    
    h = len(matrix)
    w = len(matrix[0])
    
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == "L":
                lever = [i,j]
            elif matrix[i][j] == "S":
                start = [i,j]
            elif matrix[i][j] == "E":
                end = [i,j]
                
    print(start, lever, end)
    
    def bfs(start, graph, target):
        
        deq = deque([start])
                
        visited = [[0] * w for _ in range(h)]
        
        visited[start[0]][start[1]] = 1
        
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        
        while deq:
            y, x = deq.popleft()
        
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < w and 0 <= ny < h:
                    if visited[ny][nx] == 0 and graph[ny][nx] != "X":
                        visited[ny][nx] = visited[y][x] + 1
                        deq.append([ny, nx])

                        if graph[ny][nx] == target:
                            return visited[y][x]
                        
                        
        return -1
        
    result1 = bfs(start, matrix, "L")
    
    result2 = bfs(lever, matrix, "E")
    
    print(result1, result2)
    
    if result1 == -1 or result2 == -1:
        return -1
                 
    answer = result1 + result2
    
    return answer


print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]	))
print(solution(["SELXX", "XXXXX", "XXXXX", "XXXXX", "XXXXX"]))