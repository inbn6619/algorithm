from collections import deque

M, N = map(int, input().split()) # M 가로, N 세로

tomatos = [list(map(int, input().split())) for _ in range(N)]

queue = deque()

for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 1:
            queue.append([i, j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while queue:
        y, x = queue.popleft()

        for f in range(4):
            nx = x + dx[f]
            ny = y + dy[f]

            if 0 <= nx < M and 0 <= ny < N:
                if tomatos[ny][nx] == 0:
                    tomatos[ny][nx] = tomatos[y][x] + 1
                    queue.append([ny, nx])

bfs()

result = 0

for line in tomatos:
    if 0 in line:
        print(-1)
        exit(0)
    result = max(result, max(line))

print(result - 1)