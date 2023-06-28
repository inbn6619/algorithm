def solution(game_board, table):
    from collections import deque

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


    def bfs(start, board, T, F, n, m):
        queue = deque([start])
        coor = list()
        coor.append(start)

        while queue:
            y, x = queue.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if 0 <= nx < m and 0 <= ny < n and board[ny][nx] == T:
                    coor.append([ny, nx])
                    queue.append([ny, nx])
                    board[ny][nx] = F

        return coor


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


    rotated_table2 = rotate(table)
    rotated_table3 = rotate(rotated_table2)
    rotated_table4 = rotate(rotated_table3)
        
    n = len(game_board)
    table_coor = list()
    board_coor = list()


    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                board_coor.append(bfs([i, j], game_board, 0, 1, n, n))
    
    for tab in [table, rotated_table2, rotated_table3, rotated_table4]:
        coor = list()
        for i in range(n):
            for j in range(n):
                if tab[i][j] == 1:
                    coor.append(bfs([i, j], tab, 1, 0, n, n))
        table_coor.append(coor)

    board_square = list()
    

    for i in range(len(board_coor)):
        board_square.append(func(board_coor[i]))

    def table_squ(array):
        square = list()
        for coor in array:
            square.append(func(coor))
        return square

    table_square = list()
    for coor in table_coor:
        table_square.append(table_squ(coor))

    board_check = [False] * len(board_square)
    table_check = [False] * len(table_square[0])

    for i in range(len(board_square)):
        for t in range(len(table_square)):
            for j in range(len(table_square[t])):
                if not board_check[i]:
                    if not table_check[j]:
                        if board_square[i] == table_square[t][j]:
                            board_check[i] = True
                            table_check[j] = True

    count = 0

    for num in range(len(board_square)):
        if board_check[num]:
            for i in range(len(board_square[num])):
                count += sum(board_square[num][i])

    answer = count
    return answer

game_board1 = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
game_board2 = [[0,0,0],[1,1,0],[1,1,1]]
table1 = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
table2 = [[1,1,1],[1,0,0],[0,0,0]]

game_board3 = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]

table3 = [[0, 1, 0], [1, 1, 1], [1, 0, 1]]

game_board4 = [[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

table4 = [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]

# print(solution(game_board1, table1))
# print(solution(game_board2, table2))
# print(solution(game_board3, table3))
print(solution(game_board4, table4)) # 54