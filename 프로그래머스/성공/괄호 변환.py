def func(string):
    cnt1, cnt2 = 0, 0
    
    for s in string:
        if (cnt1 + cnt2 > 0) and cnt1 == cnt2:
            break
        if s == "(":
            cnt1 += 1
        else:
            cnt2 += 1
            
    u = string[:cnt1+cnt2]
    v = string[cnt1+cnt2:]

    if u == "":
        return ""
    
    copyU = u
    for i in range(len(copyU)//2):
        copyU = copyU.replace("()", "")
    
    if not copyU:
        return u + func(v)
    else:
        uList = list(u[1:-1])
        
        for i in range(len(uList)):
            if uList[i] == "(":
                uList[i] = ")"
            else:
                uList[i] = "("
            
        
        return "(" + func(v) + ")" + ''.join(uList)
    
        

def solution(p):
    answer = func(p)
    return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
print(solution(")()(()"))