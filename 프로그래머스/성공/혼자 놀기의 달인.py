def solution(cards):
    answer = 0
    
    result = list()
    
    for i in range(len(cards)):
        
        if cards[i] != 0:
            tmp = list()
            target = cards[i]
            cards[i] = 0
            
            while target != 0:
                tmp.append(target)
                t = cards[target - 1]
                cards[target - 1] = 0
                target = t
                
            # print(cards)
            # print(tmp)
            result.append(tmp)
                
        if len(result[-1]) == len(cards):
            return 0

    # print(result)
    
    sortedResult = sorted(result, key=lambda x : len(x))
    
    answer = len(sortedResult[-1]) * len(sortedResult[-2])
    
    return answer