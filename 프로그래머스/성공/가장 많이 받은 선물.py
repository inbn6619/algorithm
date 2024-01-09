def solution(friends, gifts):
    answer = {i : 0 for i in friends}
        
    matrix = [[0] * len(friends) for i in range(len(friends))]
    
    friendsDict = {value : idx for idx, value in enumerate(friends)}
        
    for gift in gifts:
        s, g = gift.split()
        
        matrix[friendsDict[s]][friendsDict[g]] += 1
        
    numGiftDict = dict()
    
    for i in range(len(matrix)):
        
        getGift = 0
        sendGift = 0
        
        for j in range(len(matrix)):
            getGift += matrix[j][i]
            sendGift += matrix[i][j]
        
        numGiftDict[friends[i]] = sendGift - getGift
        
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                continue
            if matrix[i][j] > matrix[j][i]:
                answer[friends[i]] += 1
            elif matrix[i][j] == matrix[j][i]:
                if numGiftDict[friends[i]] < numGiftDict[friends[j]]:
                    answer[friends[j]] += 1
                elif numGiftDict[friends[i]] == numGiftDict[friends[j]]:
                    continue
                else:
                    answer[friends[i]] += 1
            else:
                answer[friends[j]] += 1
    

    
    return max(answer.values()) //2
