from collections import deque

def solution(s):
    answer = 0
    
    numList = list()
    
    length = len(s)

    if length == 1:
        return length
    
    k = 1
    
    while k <= length//2:
        deq = deque(s)

        target = 0
        result = list()
        stack = list()

        while deq:
            t = list()
            while len(t) != k and deq:
                t.append(deq.popleft())
            t = ''.join(t)
            
            if not target:
                target = t
                stack.append(target)
                continue

            if target == t:
                stack.append(target)
            else:
                if stack and len(stack) != 1:
                    result.append(str(len(stack)))

                result.append(target)
                target = t
                stack = [target]
        
        if stack[-1] == '0':
            stack.pop()
        
        if stack:
            if len(stack) != 1: result.append(str(len(stack)))
            result.append(target)



        numList.append(len(''.join(result)))
        
        # print(''.join(result), k)

        k += 1
    
    # print(numList)
    answer = min(numList)
    
    return answer


print(solution("aabbaccc"))
print(solution("abcabcabcabcdededededede"))
print(solution("s"))