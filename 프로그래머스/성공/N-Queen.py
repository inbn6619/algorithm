def solution(n):
    answer = 0
    
    from collections import deque
    
    target = [i for i in range(1, n+1)]
    
    for i in range(1, n+1):
        copiedTarget = target.copy()

        del copiedTarget[i-1]
        
        # print(i, copiedTarget)
        queue = deque([[[i], copiedTarget]])
        
        # print(queue)
        
        while queue:
            node, check = queue.popleft()
            
            if len(node) == n:
                # print(node)
                answer += 1
            
            y2 = len(node) + 1
            
            # print(node, check)

            for x2 in check:
                copiedCheck = check.copy()

                bol = True
                
                for y1, x1 in enumerate(node):
                    # print(c, idx, n)
                    if abs(x1-x2) == abs(y1+1 - y2):
                        bol = False
                        continue

                if bol:
                    copiedCheck.remove(x2)
                    # print(x1, x2, copiedCheck)
                    queue.append([node + [x2], copiedCheck.copy()])
                    # copiedCheck.append(x2)

    
    return answer