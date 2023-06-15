def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    answer = 0
    check = False
    

    def dfs(var):
        nonlocal answer
        nonlocal check
        if word == var:
            check = True
            return check
        
        if len(var) == 5:
            return

        for w in words:
            if not check:
                answer += 1
                dfs(var + w)

    test = ''
    dfs(test)

    return answer


# solution("AAAAE")
print(solution("AAAE"))
print(solution('I'))
print(solution('EIO'))

# n + 5a + 25b + 125c + 625d
# 1, 11, 111, 1111, 11111, 11112, 11113, 11114, 11115, 11120, 11121, 11122, 11123, 11124, 11125, 11130, 