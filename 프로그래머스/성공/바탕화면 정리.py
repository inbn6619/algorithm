def solution(wallpaper):
    answer = []
    
    h = len(wallpaper)
    w = len(wallpaper[0])
    
    xList = list()
    yList = list()
    
    for i in range(h):
        for j in range(w):
            if wallpaper[i][j] == "#":
                xList.append(j)
                yList.append(i)
                
    answer.append(min(yList))
    answer.append(min(xList))
    answer.append(max(yList) + 1)
    answer.append(max(xList) + 1)
    
    return answer