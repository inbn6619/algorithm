def solution(s, skip, index):
    import string
    
    alphaSet = set(string.ascii_lowercase)
    
    alphaSet -= set(skip)
    
    alphaList = sorted(list(alphaSet))
    
    print(alphaList)
    
    answer = ''
    
    for i in s:
        idx = alphaList.index(i)
        
        answer += alphaList[(idx + index) % len(alphaList)]
        
    
    
    return answer