def solution(land):
    answer = 0

    for i in range(1, len(land)):
        for j in range(4):
            target = land[i-1][j]
            
            land[i-1][j] = -1
            
            land[i][j] += max(land[i-1][0], land[i-1][1], land[i-1][2], land[i-1][3])
            
            land[i-1][j] = target
                    
    return max(land[-1])