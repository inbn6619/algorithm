from collections import deque

def solution(n):
    arrayList = [[0] * i for i in range(1, n+1)]

    status = deque(["down", "stay", "up"])
    
    cnt = 1
    
    stair = 1
    
    position = 0
    
    for i in range(n, 0, -1):
        st = status.popleft()
                
        for j in range(i, 0, -1):
            
            arrayList[stair-1][position] = cnt
            
            if st == "down":
                stair += 1
            elif st == "up":
                position -= 1
                stair -= 1
            else:
                position += 1
            cnt += 1

        if st == "down":
            stair -= 1
            position += 1
        elif st == "stay":
            stair -= 1
            position -= 2
        else:
            position += 1
            stair += 2
        
        status.append(st)

    answer = list()
    
    for arr in arrayList:
        answer.extend(arr)
    
    return answer