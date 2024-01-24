from itertools import permutations 

def solution(expression):
    answer = 0
    
    result = list()
    
    numList = list()
    
    checkSet = set()
    
    for i in expression:
        if i.isdigit():
            numList.append(i)
        else:
            result.append(int(''.join(numList)))
            numList = list()
            checkSet.add(i)
            result.append(i)
    result.append(int(''.join(numList)))
    
    checkList = list(permutations(list(checkSet), len(checkSet)))
    
    while checkList:
        check = checkList.pop()
        
        copyResult = result.copy()
        
        for c in check:
            while True:
                
                if c not in copyResult:
                    break

                target = copyResult.index(c)
                    
                n1 = copyResult[target-1]
                n2 = copyResult[target+1]

                if c == "*":
                    copyResult[target-1] = n1 * n2
                elif c == "+" :
                    copyResult[target-1] = n1 + n2
                else:
                    copyResult[target-1] = n1 - n2

                del copyResult[target+1]
                del copyResult[target]
                    
                    
        count = abs(copyResult[0])
        
        if answer < count:
            answer = count
    
    return answer

print(solution("100-200*300-500+20"	))