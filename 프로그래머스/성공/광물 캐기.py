from collections import deque

def solution(picks, minerals):
    answer = 0
        
    length = min(len(minerals), sum(picks) * 5)
        
    mDict = {'diamond': 0, 'iron': 1, 'stone':2}
    checkDict = {0:[1,1,1], 1:[5, 1, 1], 2:[25, 5, 1]}
    
    result = list()
    d, i, s= 0, 0, 0
    for j in range(length):
        d += checkDict[0][mDict[minerals[j]]]
        i += checkDict[1][mDict[minerals[j]]]
        s += checkDict[2][mDict[minerals[j]]]
        
        if (j + 1 ) % 5 == 0 or (j+1) == length:
            result.append([d, i, s])
            d, i, s= 0, 0, 0
            
    sortedResult = sorted(result, key=lambda x: x[2], reverse=True)
    
    # print(result)
    # print(sortedResult)
    
    for r in sortedResult:
        for i in range(3):
            if picks[i]:
                picks[i] -= 1
                answer += r[i]
                # print(i, r[i])
                break

    return answer

print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]	))
print(solution([0, 1, 1],["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))