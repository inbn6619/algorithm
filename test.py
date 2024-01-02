def solution(cards1, cards2, goal):
    answer = 'No'
    
    c1 = 0
    c2 = 0
    
    check = True
    
    for i in goal:
        if cards1[c1] == i and len(cards1) > c1:
            c1 += 1
            continue
        if cards2[c2] == i and len(cards2) > c2:
            c2 += 1
            continue
        
        check = False
        break

    if check:
        answer = "Yes"
    
    return answer

print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink" ], ["want", "to"], ["i", "want", "to", "drink", "water"]))