def solution(n, m, section):
    answer = 0
    
    from collections import deque
    
    deq = deque(section)
    
    
    while deq:
        start = deq.popleft()
        
        answer += 1
        
        
        while deq:
            end = deq.popleft()
                        
            if start + m - 1 < end:
                deq.appendleft(end)
                break
            
        
    return answer