from collections import deque

def solution(skill, skill_trees):
    answer = 0
   
    for i in skill_trees:
        deq = deque(skill)
        
        check = True

        for j in i:
            if j in skill:
                if j == deq[0]:
                    deq.popleft()
                else:
                    check = False
                    break
                    
        if check:
            answer += 1
                    

    
    return answer