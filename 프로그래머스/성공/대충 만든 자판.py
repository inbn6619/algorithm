def solution(keymap, targets):
    answer = []
    
    from collections import deque
    
    
    for j in targets:
        deq = deque(j)
        
        minValue = list()
        
        check = True
    
        while deq:
            target = deq.popleft()
            
            numList = list()

            for i in keymap:
                
                findTarget = i.find(target)
                
                if findTarget != -1:
                    numList.append(findTarget)

            if numList:
                minValue.append(min(numList))
            else:
                check = False
                break
                
        if check:
            answer.append(sum(minValue) + len(minValue))
        else:
            answer.append(-1)

    return answer