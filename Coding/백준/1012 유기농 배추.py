import sys

sys.setrecursionlimit(10000) # 재귀함수 재귀 한계수치 늘리는 코드 (없을 시 런타임에러)

def dfs(grahp, y, x):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    if grahp[y][x] == 1:
        grahp[y][x] = 0

        for f in range(4):
            nx = x + dx[f]
            ny = y + dy[f]

            if 0<= nx < M and 0<= ny < N:
                if grahp[ny][nx] == 1:
                    dfs(grahp, ny, nx)

T = int(input())

for t in range(T):

    bugs = 0

    M, N, K = map(int, input().split()) # 가로, 세로, 배추 위치 개수

    matrix = [[0] * (M) for _ in range(N)]

    for k in range(K):
        X, Y = map(int, input().split())
        matrix[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                bugs += 1
                dfs(matrix, i, j)

    print(bugs)

