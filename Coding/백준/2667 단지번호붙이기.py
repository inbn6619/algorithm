N = int(input()) # 정사각형 한 변의 길이

matrix = [[int(i) for i in list(input())] for _ in range(N)]

# print(matrix)

houses = list()

def dfs(grahp, y, x):

    if grahp[y][x] == 1:
        grahp[y][x] = 0 # 방문
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0<= ny < N:
                if grahp[ny][nx] == 1:
                    houses[-1] += 1
                    dfs(grahp, ny, nx)

for j in range(N):
    for k in range(N):
        if matrix[j][k] == 1:
            houses.append(1)
            dfs(matrix, j, k)


houses.sort()
print(len(houses))
for num in houses:
    print(num)