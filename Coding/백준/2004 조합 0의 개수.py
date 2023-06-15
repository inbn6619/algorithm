# nCr == n!/(n-r)!r!

def get_num(n, i):
    num = 0
    while n != 0:
        n = n // i
        num += n
    return num

N, M = map(int, input().split())

two = get_num(N, 2) - get_num(N - M, 2) - get_num(M, 2)
five = get_num(N, 5) - get_num(N - M, 5) - get_num(M, 5)

print(min(two, five))
