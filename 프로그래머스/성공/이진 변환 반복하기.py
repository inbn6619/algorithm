def solution(s):
    count, result = 0, 0

    def check(s, n):
        nonlocal count, result  # count와 result를 외부 함수의 변수로 사용
        if n == 1:
            return
        
        num = s.count("0")
        n -= num
        s = "{0:b}".format(n)
        
        count += 1
        result += num
        
        check(s, len(s))
    
    check(s, len(s))
    
    return [count, result]

print(solution("110010101001"))