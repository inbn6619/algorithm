def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(arrayA, arrayB):
    answer = 0
    
    checkArrayA = arrayA.copy()
    checkArrayB = arrayB.copy()
    
    gcdA = arrayA.pop()
    
    gcdB = arrayB.pop()

    while arrayA:
        gcdA = gcd(gcdA, arrayA.pop())
    
    while arrayB:
        gcdB = gcd(gcdB, arrayB.pop())
            
    checkA = True
    checkB = True
    
    for i in range(len(checkArrayA)):
        if checkArrayA[i] % gcdB == 0:
            checkB = False

    for i in range(len(checkArrayB)):
        if checkArrayB[i] % gcdA == 0:
            checkA = False
    
    if checkA and checkB:
        answer = max(gcdA, gcdB)
    elif checkA:
        answer = gcdA
    elif checkB:
        answer = gcdB

    return answer