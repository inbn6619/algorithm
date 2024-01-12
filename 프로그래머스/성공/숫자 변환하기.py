from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    answer = -1
    
    deq = deque([x])    
    
    resultDict = {i:0 for i in range(1000001)}

    while deq:
        q = deq.popleft()
        
        if 0<= q + n <= 1000000 and resultDict[q + n] == 0: 
            resultDict[q + n] = resultDict[q] + 1
            deq.append(q + n)
        if 0<= q * 2 <= 1000000 and resultDict[q * 2] == 0:
            resultDict[q * 2] = resultDict[q] + 1
            deq.append(q * 2)
        if 0<= q * 3 <= 1000000 and resultDict[q * 3] == 0:
            resultDict[q * 3] = resultDict[q] + 1
            deq.append(q * 3)
            
    if resultDict[y]:
        answer = resultDict[y]
    else:
        answer = -1
    
    return answer

# print(solution(10, 40, 5))
print(solution(2, 5, 4))