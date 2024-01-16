def solution(numbers):
    answer = []
    
    for num in numbers:
        if num % 2 == 0:
            answer.append(num+1)
        else:
            answer.append(num + ((num ^ num + 1) >> 2) + 1)    
    
    return answer