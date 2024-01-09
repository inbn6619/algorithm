def solution(players, callings):
    
    d = {players[i] : i + 1 for i in range(len(players))}
    
    for call in callings:
        d[call] -= 1
        d[players[d[call] - 1]] += 1
        
        players[d[call] - 1], players[d[call]] = call, players[d[call] - 1]
         
    d = sorted(d.items(), key=lambda x : x[1])
    
    answer = [i[0] for i in d]
    
    return answer