# pppp = p * 1111
# pppq = (10 * p + q)**2
# ppqq = (p + q) * |p - q|
# ppqr = q * r
# pqrw = min([p, q, r, w])


def solution(a, b, c, d):
    answer = 0

    a, b, c, d = sorted([a, b, c, d])

    if a == d:
        answer = a * 1111
    elif sum([a, b, c]) == a * 3:
        answer = (10 * a + d)**2
    elif sum([b, c, d]) == d * 3:
        answer = (10 * d + a)**2
    elif a == b and c == d:
        answer = (a + d) * abs(a - d)
    elif a != b != c != d:
        answer = min([a, b, c, d])
    else:
        if a == b:
            answer = c * d
        elif b == c:
            answer = a * d
        else:
            answer = a * b


    return answer

print(solution(4, 1, 4, 4))
print(solution(6, 3, 3, 6))