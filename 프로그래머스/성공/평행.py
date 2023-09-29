def func(dot1, dot2, dot3, dot4):
    ch1 =  (dot1[1] - dot2[1]) / (dot1[0] - dot2[0])
    ch2 =  (dot3[1] - dot4[1]) / (dot3[0] - dot4[0])
    
    if ch1 == ch2:
        return 1
    else:
        return 0

def solution(dots):
    answers = list()
    
    answers.append(func(dots[0], dots[1], dots[2], dots[3]))
    answers.append(func(dots[0], dots[2], dots[1], dots[3]))
    answers.append(func(dots[0], dots[3], dots[1], dots[2]))
    
    answer = max(answers)
    
    return answer