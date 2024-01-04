def solution(s):    
    start = s[0]
    
    result = list()
    
    string = start
    
    x, y = 1, 0
    
    for i in s[1:]:
        
        if x == y:
            result.append(string)
            start = i
            string = start
            x = 1
            y = 0
            continue
        else:
            string += i
        
        if start == i:
            x += 1
        else:
            y += 1
    
    if x == y:
        result.append(string)
    else:
        result.append(" ")
            
            
    print(result)
    
    answer = len(result)
    
    return answer