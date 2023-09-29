def solution(polynomial):
    array = polynomial.split(' + ')

    num = 0
    X = 0

    for i in array:
        if i == 'x':
            i = '1x'
        if i[-1] == 'x':
            X += int(i[:-1])
        else:
            num += int(i)

    if X == 0:
        answer = str(num)
        return answer
    elif X == 1:
        X = 'x'
    else:
        X = str(X) + 'x'
    
    if num == 0:
        answer = X
    else:
        answer = '%s + %d' % (X, num)

    return answer

polynomial1 = "3x + 7 + x"
polynomial2 = "x + x + x"
polynomial3 = '1'
polynomial4 = 'x'
polynomial5 = ''

print(solution(polynomial1))
print(solution(polynomial2))
print(solution(polynomial3))
print(solution(polynomial4))
# print(solution(polynomial5))