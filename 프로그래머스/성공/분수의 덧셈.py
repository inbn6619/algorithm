def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer = denom1 * numer2 + denom2 * numer1

    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    gcd = gcd(numer, denom)
    
    answer = [numer//gcd, denom//gcd]
    return answer



solution(1, 2, 3, 4)