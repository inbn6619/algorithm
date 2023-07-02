def solution(priorities, location):
    from collections import deque
    
    queue = deque(priorities)
    count = 0
    
    while queue:
        
        start = queue.popleft()

        if len(queue):
            max_num = max(queue)
        
        if start < max_num:
            queue.append(start)
            if location == 0:
                location = len(queue)
        else:
            count += 1
            if location == 0:
                break
                
        location -= 1
    
    
    answer = count
    return answer

print(solution([3, 2, 1], 2))