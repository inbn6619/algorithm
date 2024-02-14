from math import sqrt

def solution(k, d):
    answer = 0
    target = d ** 2
        
    for i in range(0, d+1, k):
        t = target - i ** 2
        answer += sqrt(t) // k + 1

    return answer
