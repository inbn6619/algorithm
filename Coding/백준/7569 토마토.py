import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split()) # M = 가로, N = 세로, H = 높이
queue = deque()

matrix = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

for h in range(H):
    for n in range(N):
        for m in range(M):
            if matrix[h][n][m] == 1:
                queue.append([h, n, m])

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    while queue:
        z, y, x = queue.popleft()
        for f in range(6):
            nx = x + dx[f]
            ny = y + dy[f]
            nz = z + dz[f]

            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if matrix[nz][ny][nx] == 0:
                    matrix[nz][ny][nx] = matrix[z][y][x] + 1
                    queue.append([nz, ny, nx])

bfs()

result = 0

for a in matrix:
    for b in a:
        if 0 in b:
            print(-1)
            exit(0)
        result = max(result, max(b))

print(result - 1)