def solution(topping):
    answer = 0
    
    toppingDict = {x : 0 for x in topping}
    
    for t in topping:
        toppingDict[t] += 1
    
    toppingSet = set()
    
    for i in topping:
        toppingDict[i] -= 1
        if toppingDict[i] == 0:
            del toppingDict[i]
        toppingSet.add(i)
        
        if len(toppingSet) == len(toppingDict):
            answer += 1


    return answer