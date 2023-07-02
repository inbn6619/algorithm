def solution(bridge_length, weight, truck_weights):
    from collections import deque
    answer = 0
    start = deque(truck_weights)
    end = list()
    bridge = deque([[] for _ in range(bridge_length)])
    
    while True:
        answer += 1
        
        if end == truck_weights:
            break
        
        if start:
            if weight >= start[0]:
                truck = start.popleft()
                weight -= truck
                bridge[-1].append(truck)
                
        if bridge[0]:
            for i in bridge[0]:
                weight += i
                end.append(i)
            
            bridge[0] = []

        bridge.append(bridge.popleft())
            
    return answer

# print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))