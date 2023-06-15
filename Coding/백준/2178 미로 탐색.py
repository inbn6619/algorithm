dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(grahp, y, x):
    from collections import deque
    queue = deque()
    queue.append((y, x))
    
    while queue:
        y, x = queue.popleft()

        for n in range(4):
            nx = x + dx[n]
            ny = y + dy[n]

            if 0<= nx < M and 0<= ny < N:
                if grahp[ny][nx] == 1:
                    queue.append((ny, nx))
                    grahp[ny][nx] = grahp[y][x] + 1
            
    return grahp[N-1][M-1]
                    


N, M = map(int, input().split())

matrix = [[int(i) for i in list(input())] for _ in range(N)]

print(bfs(matrix, 0, 0))