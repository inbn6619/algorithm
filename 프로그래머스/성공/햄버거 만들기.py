def solution(ingredient):
    
    target = [1, 2, 3, 1]
    
    answer = 0
    
    stack = list()

    for i in ingredient:
        if stack[-4:] == target:
            answer += 1
            del stack[-4:]
        stack.append(i)
  
    if stack[-4:] == target:
        answer += 1
        del stack[-4:]
        
    return answer