def solution(n):
    answer = []
    
    def hanoi(num, a, b, c):
        if num == 1:
            answer.append([a, c])
        else:
            hanoi(num-1, a, c, b)
            answer.append([a, c])
            hanoi(num-1, b, a, c)

    hanoi(n, 1, 2, 3)
    
    return answer

print(solution(2))