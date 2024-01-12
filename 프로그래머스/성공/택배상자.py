from collections import deque

def solution(order):
    answer = 0
    
    stack = list()
    
    truck = list()
    
    boxList = deque([i for i in range(1, len(order) + 1)])
        
    for i in order:
        if stack:
            if stack[-1] == i:
                truck.append(stack.pop())
                continue
        if i in boxList:
            while boxList:
                target = boxList.popleft()

                if target == i:
                    truck.append(target)
                    break
                else:
                    stack.append(target)
        else:
            break
                
    answer = len(truck)

    return answer

print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))