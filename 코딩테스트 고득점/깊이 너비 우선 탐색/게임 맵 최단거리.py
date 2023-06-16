def solution(maps):

    height = len(maps)
    width = len(maps[0])

    answer = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    board = [[0] * width for _ in range(height)]
    
    def bfs(start):
        from collections import deque
        queue = deque([start])
        board[start[1]][start[0]] = 1

        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if 0 <= nx < width and 0 <= ny < height and maps[ny][nx] == 1 and board[ny][nx] == 0:
                    queue.append([nx, ny])
                    board[ny][nx] = board[y][x] + 1
                    maps[ny][nx] = 0

        if board[height-1][width-1] == 0:
            return -1
        else:
            return board[height-1][width-1]

    answer = bfs([0, 0])

    return answer

map1 = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,1],
        [0,0,0,0,1]
        ] # 11
map2 = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,0],
        [0,0,0,0,1]
        ] # -1

print(solution(map1))
print(solution(map2))