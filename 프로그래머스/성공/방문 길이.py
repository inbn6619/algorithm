def solution(dirs):
    answer = 0
    
    x, y = 0, 0
    
    nx, ny = 0, 0
    
    resultSet = set()
    
    for d in dirs:
        nx, ny = x, y
        
        if d == "U":
            ny += 1
        elif d == "D":
            ny -= 1
        elif d == "R":
            nx += 1
        else:
            nx -= 1
            
        if abs(nx) > 5 or abs(ny) > 5:
            continue
                
        resultSet.add((x, y, nx, ny))
        resultSet.add((nx, ny, x, y))
        x, y = nx, ny

    
    return len(resultSet) // 2