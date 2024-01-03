def solution(dartResult):
    
    result = list()
    
    alphaDict = {
        "S" : 1,
        "D" : 2,
        "T" : 3
    }
    
    
    num = ""
    
    for i in dartResult:
        if i.isdigit():
            num += i
        elif i.isalpha():
            result.append(int(num) ** alphaDict[i])
            num = str()
        else:
            if i == "#":
                result[-1] *= -1
            else:
                result[-1] *= 2
                
                if len(result) >= 2:
                    result[-2] *= 2
                
            
    answer= sum(result)    
    
    return answer