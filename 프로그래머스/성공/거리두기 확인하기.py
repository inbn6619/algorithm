

def solution(places):
    answer = []
    
    dx = [1, 0, -1, 0,
          0, -2, 0, 2,
          1, -1, 1, -1]
    dy = [0, 1, 0, -1,
          -2, 0, 2, 0,
          1, 1, -1, -1]
    
    def checkDirection(y, x, dy, dx):

        if dy != 0 and dx != 0:
            # 8방위 중 대각선
            if dy == 1 and dx == 1:
                if matrix[y-1][x] != "X" or matrix[y][x-1] != "X":
                    return False
            elif dy == 1 and dx == -1:
                if matrix[y-1][x] != "X" or matrix[y][x+1] != "X":
                    return False
            elif dy == -1 and dx == 1:
                if matrix[y+1][x] != "X" or matrix[y][x-1] != "X":
                    return False
            else:
                if matrix[y+1][x] != "X" or matrix[y][x+1] != "X":
                    return False
            
        else:
            if abs(dx) == 2 or abs(dy) == 2:
                # 4방위 + 1
                if abs(dx) > abs(dy):
                    if dx < 0:
                        if matrix[y][x + 1] != "X":
                            return False
                    else:
                        if matrix[y][x - 1] != "X":
                            return False
                else:
                    if dy < 0:
                        if matrix[y + 1][x] != "X":
                            return False
                    else:
                        if matrix[y - 1][x] != "X":
                            return False
            
            else:
                # 4방위
                return False
        return True
                
        
        
    
    def checkLength(y, x):
        for i in range(12):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 5 and 0 <= ny < 5:
                if matrix[ny][nx] == "P":
                    result = checkDirection(ny, nx, dy[i], dx[i])
                    if not result:
                        nonlocal check
                        check = False
                        return
    
    for p in places:
        matrix = [list(i) for i in p]
        # print(matrix)
        
        # copiedMatrix = matrix.copy()
        
        check = True
        
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == "P":
                    checkLength(i, j)
        if not check:
            answer.append(0)
        else:
            answer.append(1)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]	))