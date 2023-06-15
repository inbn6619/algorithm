def solution(A, B):
    check = A
    answer = 0

    while True:
        if A == B:
            break

        A = A[-1] + A[:-1]

        if check == A:
            answer = -1
            break

        answer += 1

    return answer

A1 = 'hello'
B1 = 'ohell'
A2 = 'apple'
B2 = 'elppa'
B3 = 'abc'
A3 = 'abc'
print(solution(A1, B1))
print(solution(A2, B2))
print(solution(A3, B3))