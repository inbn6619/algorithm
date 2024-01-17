def solution(number, k):
    answer = []
    
    for num in number:
        if not answer:
            answer.append(num)
            continue
        
        while k > 0 and answer[-1] < num:
            answer.pop()
            k -= 1
            
            if not answer or k <= 0:
                break

        answer.append(num)
        
        if len(answer) == len(number) - k:
            break

    return ''.join(answer)

print(solution("1924", 2))