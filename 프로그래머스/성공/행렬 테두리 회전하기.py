def solution(rows, columns, queries):
    answer = []
    
    cnt = 0
    
    matrix = [[] for _ in range(rows)]
        
    for m in matrix:
        for j in range(columns):
            cnt += 1
            m.append(cnt)
            
    def processQueries(query):
        y1, x1, y2, x2 = query
        h = (y2 - y1 + 1)
        w = (x2 - x1 + 1)
        
        y, x = y1-1, x1-1
        
        target = matrix[y][x]
            
        result = [target]
                
        for _ in range(w-1):
            x += 1
            t = matrix[y][x]
            matrix[y][x] = target
            target = t
            result.append(target)
            
        for _ in range(h-1):
            y += 1
            t = matrix[y][x]
            matrix[y][x] = target
            target = t
            result.append(target)
            
        for _ in range(w-1):
            x -= 1
            t = matrix[y][x]
            matrix[y][x] = target
            target = t
            result.append(target)
    
        for _ in range(h-1):
            y -= 1
            t = matrix[y][x]
            matrix[y][x] = target
            target = t
            result.append(target)
        
        return min(result)
    
    for q in queries:
        answer.append(processQueries(q))

    return answer

    
