from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())

matrix = [list(input()) for _ in range(N)]

visited1 = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]



def dfs(y, x, visited):
    queue = deque()
    queue.append([y, x])
    color = matrix[y][x]
    visited[y][x] = True

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0<= ny < N:
                if color == matrix[ny][nx]:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        queue.append([ny, nx])

cnt1 = 0
cnt2 = 0

for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            dfs(i, j, visited1)
            cnt1 += 1

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'G':
            matrix[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if not visited2[i][j]:
            dfs(i, j, visited2)
            cnt2 += 1

print(cnt1, cnt2)