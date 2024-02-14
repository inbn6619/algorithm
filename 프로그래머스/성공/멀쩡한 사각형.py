def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(w,h):

    _gcd = gcd(w, h)
    
    square = w * h
    
    cnt = 0
    
    answer = square - _gcd * (w//_gcd * h//_gcd - (w//_gcd -1) * (h//_gcd - 1))
    
    return answer
