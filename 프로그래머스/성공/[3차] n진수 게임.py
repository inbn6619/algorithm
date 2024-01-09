def solution(n, t, m, p):
    answer = ''
    
    check = ''

    for i in range(m * t):
        
        result = ''
        
        if i == 0:
            result = '0'
            check += result
            continue

        while i > 0:
            r = i % n

            if r < 10:
                result = str(r) + result
            else:
                result = chr(ord('A') + r - 10) + result
            i = i // n

        
        check += result
        
        cnt = 0
    for a in range(p-1, len(check), m):
        answer += check[a]
        cnt += 1
        if cnt == t:
            break

    return answer