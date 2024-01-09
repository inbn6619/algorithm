def solution(today, terms, privacies):
    answer = []
    
    moon = 28 * 12
        
    today = list(map(int, today.split(".")))
    
    target = (today[1] - 1) * 28 + today[2]
        
    d = dict()
    
    for i in terms:
        a, i = i.split()
        d[a] = int(i)
            
    for idx, s in enumerate(privacies):
        
        s, alpha = s.split()
            
        s = list(map(int, s.split(".")))
        
        if today[0] > s[0]:
            result =  moon * (today[0] - s[0]) - ((s[1]-1) * 28 + s[2]) + target
        else:
            result = target - ((s[1]-1) * 28 + s[2])
                    
        if result >= d[alpha] * 28:
            answer.append(idx+1)
        
    
    return answer