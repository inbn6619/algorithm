import math

def solution(r1, r2):
    answer = 0
    
    target1 = r1 ** 2
    target2 = r2 ** 2
    
    for i in range(1, r2+1):
        maxY = math.floor(math.sqrt(target2 - i**2))
        minY = math.ceil(math.sqrt(target1 - i**2)) if r1 > i else 0

        print(i, maxY+1, minY)

        answer += maxY-minY + 1
        # print(maxY, minY)
    
    answer *= 4
    
    return answer

print(solution(2, 3))