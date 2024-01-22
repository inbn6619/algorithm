def solution(storey):
    answer = 0
    
    num = 10
    
    while storey > 0:
        target = storey % num
        storey //= num
        
        if target > (num//2):
            target = num - target
            storey += 1
        elif target == 5:
            if storey % num >= 5:
                storey += 1

        
        answer += target
        
    
    return answer