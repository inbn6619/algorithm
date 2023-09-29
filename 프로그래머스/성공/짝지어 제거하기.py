def solution(s):
    stack = list()

    char = ""

    for i in s:
        if char != i:
            stack.append(i)
        else:
            stack.pop()

        if stack:
            char = stack[-1]
        else:
            char = ""

    if stack:
        answer = 0
    else:
        answer = 1

    return answer

print(solution("baabaa"))
print(solution("cdcd"))