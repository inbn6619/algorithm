from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    deq1 = deque(queue1)
    deq2 = deque(queue2)
    
    s1 = sum(queue1)
    s2 = sum(queue2)
    
    maxElements = len(deq1) + len(deq2)
    
    check = False
    
    for i in range(maxElements * 2 + 1):
        if s1 > s2:
            t1 = deq1.popleft()
            s1 -= t1
            s2 += t1
            deq2.append(t1)

        elif s2 > s1:
            t2 = deq2.popleft()
            s1 += t2
            s2 -= t2
            deq1.append(t2)
        else:
            print(s1, s2)
            check = True
            break
        answer += 1
        
    print(answer, maxElements, check)
    
    if answer == maxElements * 2 + 1 and check != True:
        answer = -1
    
    return answer
