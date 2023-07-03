def solution(prices):
    answer = [0] * len(prices)
    stack = [0]
    
    for i in range(1, len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            prev = stack.pop()
            answer[prev] = i - prev
        stack.append(i)
    
    for num in stack:
        answer[num] = i - num
    
    
    
    return answer

# print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]
# print(solution([2, 2, 3, 1, 5])) # [3, 2, 1, 1, 0]
# print(solution([1, 2, 3, 4, 1] )) #  [4, 3, 2, 1, 0]
# print(solution([5, 4, 3, 2, 5])) # [1, 1, 1, 1, 0]
# print(solution([1, 2, 3, 2, 3, 1])) # [5, 4, 1, 2, 1, 0]
print(solution([3, 4, 5, 3, 4, 1]))