def solution(numbers):
    answer = [-1] * len(numbers)
    
    stack = list()
    
    for idx, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(idx)
    
    return answer