def solution(brown, yellow):
    carpet = brown + yellow

    for i in range(brown, 0, -1):
        if yellow % i == 0:
            j = yellow//i
            if carpet == (i+2)*(j+2):
                return [i + 2, j + 2]
    

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))

# n, m = map(int, input().split())

# matrix = [[0] * n for _ in range(m)]
# 48 == 4*12, 8*6, 16*3, 48*1
# yellow == y*x
# brown == 4 + 2y + 2x
# matrix == xy + 2(x+y) + 4
# matrix = (y+2)(x+2)
