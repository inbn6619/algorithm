N = int(input())
num = int(input())

matrix = [[0] * N for _ in range(N)]

ans = list()

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def snail(y, x, length, number):
    if length == 0:
        matrix[y][x] = number
        return
    
    for i in range(4):
        for _ in range(length):
            matrix[y][x] = number
            x += dx[i]
            y += dy[i]
            number -= 1

    snail(y + 1, x + 1, length - 2, number)

snail(0, 0, N -1, N**2)

for i in range(N):
    print(' '.join(map(str, matrix[i])))
    if num in matrix[i]:
        idx = matrix[i].index(num)
        ans.extend([i + 1, idx + 1])

print(' '.join(map(str, ans)))

# print(ans[0], ans[1])