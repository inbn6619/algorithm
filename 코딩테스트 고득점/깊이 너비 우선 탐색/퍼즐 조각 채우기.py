def solution(game_board, table):
    from collections import deque

    n = len(game_board)
    table_coor = list()
    board_coor = list()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    

    def rotate(array):
        num = len(array)
        m = len(array[0])
        result = [[0] * num for _ in range(m)]
        for i in range(m):
            for j in range(num -1, -1, -1):
                result[i][j] = array[num-1 -j][i]
        return result
    
    table_R = rotate(table)
    table_L = rotate(rotate(table_R))

    def bfs(start, board, T, F):
        queue = deque([start])
        coor = list()
        coor.append(start)

        while queue:
            y, x = queue.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if 0 <= nx < n and 0 <= ny < n and board[ny][nx] == T:
                    coor.append([ny, nx])
                    queue.append([ny, nx])
                    board[ny][nx] = F

        return coor

    for tab in [table, table_R, table_L]:
        coors = list()
        for i in range(n):
            for j in range(n):
                if tab[i][j] == 1:
                    tab[i][j] = 0
                    coors.append(bfs([i, j], tab, 1, 0))
                    
        table_coor.append(coors)


    for a in range(n):
        for b in range(n):
            if game_board[a][b] == 0:
                game_board[a][b] = 1
                board_coor.append(bfs([a, b], game_board, 0, 1))

    def func(array):
        y, x = list(), list()
        for coor in array:
            x.append(coor[1])
            y.append(coor[0])

        square = [[0] * (max(x) - min(x) + 1) for _ in range(max(y) - min(y) + 1)]

        for coor in array:
            coor[1] -= min(x)
            coor[0] -= min(y)
            square[coor[0]][coor[1]] = 1

        return square

    board_square = list()
    table_square = [[0] * len(table_coor[0]) for _ in range(len(table_coor))]

    for b_coor in board_coor:
        board_square.append(func(b_coor))
    table, tables = table_coor[0], table_coor[1:]

    table_square[0] = [func(i) for i in table]

    for tab in range(1, len(tables) + 1):
        for t_coor in tables[tab -1]:
            square = func(t_coor)
            if rotate(square) in table_square[0]:
                table_square[tab][table_square[0].index(rotate(square))] = square
            else:
                table_square[tab][table_square[0].index(rotate(rotate(rotate(square))))] = rotate(rotate(rotate(square)))

    checklist = [[False] * len(board_square)]

    # def dfs(arr1, arr2, num):
    #     n = len(arr1)
    #     m = len(arr1[0])

    #     for i in range(n):
    #         for j in range(m):
                

        

    for i in range(len(board_square)):
        for j in range(len(table_square)):
            a, b, c, d = len(board_square[0]), len(board_square[0][0]), len(table_square[0]), len(table_square[0][0])
            if a >= c and b >= d:
                if board_square[i] == table_square[i]:
                    checklist[i] = True
                



    answer = -1
    return answer

game_board1 = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
game_board2 = [[0,0,0],[1,1,0],[1,1,1]]
table1 = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
table2 = [[1,1,1],[1,0,0],[0,0,0]]

print(solution(game_board1, table1))
print(solution(game_board2, table2))