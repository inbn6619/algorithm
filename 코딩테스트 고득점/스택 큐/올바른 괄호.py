def solution(s):
    from collections import deque
    answer = True

    queue = deque(s)

    cnt1, cnt2 = 0, 0

    while queue:
        tmp = queue.popleft()

        if tmp == '(':
            cnt1 += 1
        else:
            cnt2 += 1
        
        if cnt1 == cnt2:
            cnt1, cnt2 = 0, 0
        if cnt2 > cnt1:
            answer = False
    if cnt1 != cnt2:
        answer = False

    
    

    return answer


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))