def solution(n):
    answer = ''
    
    country = ["4", "1", "2"]
    
    while n > 0:
        print(n)
        answer = country[n%3] + answer
        
        if n % 3 == 0:
            n -= 1
        n = n // 3

    return answer