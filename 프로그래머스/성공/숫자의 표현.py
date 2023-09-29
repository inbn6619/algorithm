def solution(n):
    count = 1
    result = [0]
    num = n
    
    while num > 0:
        start = num // count
        number = start
        while start <= n:
            
            if start == n:
                result[0] += 1
                break

            number += 1
            start += number
            
        count += 1
        num = num - (count - 1)

    answer = result[0]
    return answer

print(solution(15))