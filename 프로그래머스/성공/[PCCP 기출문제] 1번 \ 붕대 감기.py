def solution(bandage, health, attacks):    
    maxHealth = health
    curHealth = health
    
    banTime = 0
    
    for attack in attacks:
        
        print(curHealth)
        
        if curHealth <= 0:
            return -1
        
        time = (attack[0] - banTime) // bandage[0]
        outtime = (attack[0] - banTime) % bandage[0]
        
        if time > 0:
            curHealth += time * bandage[2] + time * bandage[0] * bandage[1] + outtime * bandage[1]
        else:
            curHealth += outtime * bandage[1]
        
        banTime = attack[0] + 1
 
        if curHealth > maxHealth:
            curHealth = maxHealth
        
        curHealth -= attack[1]
    
        
    print("result :", curHealth)
    
    if curHealth <= 0:
        return -1
    else:
        answer = curHealth
    
    return answer