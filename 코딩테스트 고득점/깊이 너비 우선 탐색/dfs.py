def solution(maps):

    n = len(maps)
    m = len(maps[0])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    answer = list()
    board = [[0] * n for _ in range(n)]
    cnt = 1

    def dfs(x, y):
        nonlocal cnt
        
        board[y][x] = cnt
        maps[y][x] = 0
        cnt += 1

        if [x, y] == [n-1, m-1]:
            answer.append(board[y][x])

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<= nx < n and 0<= ny < n and maps[ny][nx] == 1:

                dfs(nx, ny)

                board[ny][nx] = 0
                maps[ny][nx] = 1
                cnt -= 1

    dfs(0, 0)

    if not answer:
        answer = [-1]

    return min(answer)


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