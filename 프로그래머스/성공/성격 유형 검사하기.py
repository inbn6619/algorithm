def solution(survey, choices):
    answer = ''
    
    charList = ["R", "T", "C", "F", "J", "M", "A", "N"]
        
    charDict = dict()
    
    for c in charList:
        charDict[c] = 0
    
    
    for i in range(len(survey)):
        characters = list(survey[i])
        
        score = choices[i] - 4
        
        if score > 0:
            charDict[characters[1]] += score
        else:
            charDict[characters[0]] -= score
    
    for j in range(2, len(charList)+1, 2):
        characters = sorted(charList[j-2:j])
        
        s1 = charDict[characters[0]]
        s2 = charDict[characters[1]]
        
        if s1 == s2 or s1 > s2:
            answer += characters[0]
        else:
            answer += characters[1]
        
    
    return answer