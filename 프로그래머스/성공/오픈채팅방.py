def solution(record):
    answer = []
    
    userName = dict()
    
    commandList = list()
    
    for r in record:
        r = r.split(' ')
        
        if r[0] == "Leave":
            c, u = r
            commandList.append(c + ' ' + u)    
        else:
            c, u, n = r
            
            userName[u] = n

            commandList.append(c + ' ' + u)
            
    for com in commandList:
        c, u = com.split(' ')
        
        if c == "Enter":
            target = " 들어왔습니다."
        elif c == "Leave":
            target = " 나갔습니다."
        else:
            continue
        
        answer.append(userName[u]+ "님이" + target)

    
    return answer