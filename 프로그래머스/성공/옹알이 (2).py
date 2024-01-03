def solution(babbling):
    answer = 0

    checkList = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        for j in checkList:
            if j in i and j*2 not in i:
                i = i.replace(j, " ")
            
        print(i)
        if i.isspace():
            answer += 1
    
    
    return answer